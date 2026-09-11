from __future__ import annotations

import sqlite3

from fastapi.testclient import TestClient

from app.services import volume_service


def test_monthly_volume_excludes_cancelled(connection: sqlite3.Connection) -> None:
    result = volume_service.get_monthly_volume(connection)

    assert result.total_pieces == 260
    assert all(item.total_pieces != 999 for item in result.items)


def test_monthly_volume_groups_by_month_and_office(connection: sqlite3.Connection) -> None:
    result = volume_service.get_monthly_volume(connection)

    months = {item.month for item in result.items}
    assert months == {"2026-01", "2026-02"}


def test_monthly_volume_filtered_by_region(connection: sqlite3.Connection) -> None:
    result = volume_service.get_monthly_volume(connection, region="KHH")

    assert result.items == []
    assert result.total_pieces == 0


def test_monthly_volume_filtered_by_office(connection: sqlite3.Connection) -> None:
    result = volume_service.get_monthly_volume(connection, office_code="100")

    assert {item.office_code for item in result.items} == {"100"}
    assert result.total_pieces == 150


def test_volume_endpoint_returns_200(client: TestClient) -> None:
    response = client.get("/api/v1/volume")

    assert response.status_code == 200
    assert response.json()["total_pieces"] == 260
