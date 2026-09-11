from __future__ import annotations

import sqlite3

from fastapi.testclient import TestClient

from app.services import sla_service


def test_sla_counts_only_delivered(connection: sqlite3.Connection) -> None:
    result = sla_service.get_sla(connection)

    assert [item.office_code for item in result.items] == ["800"]
    assert result.items[0].delivered_count == 3


def test_sla_applies_t_plus_2_threshold(connection: sqlite3.Connection) -> None:
    result = sla_service.get_sla(connection)

    office = result.items[0]
    assert office.on_time_count == 2
    assert office.on_time_rate == 66.67


def test_sla_overall_rate(connection: sqlite3.Connection) -> None:
    result = sla_service.get_sla(connection)

    assert result.overall_on_time_rate == 66.67


def test_sla_filtered_by_region(connection: sqlite3.Connection) -> None:
    assert sla_service.get_sla(connection, region="KHH").items[0].delivered_count == 3
    assert sla_service.get_sla(connection, region="TPE").items == []


def test_sla_filtered_by_month(connection: sqlite3.Connection) -> None:
    january = sla_service.get_sla(connection, month="2026-01")
    february = sla_service.get_sla(connection, month="2026-02")

    assert january.overall_on_time_rate == 50.0
    assert february.overall_on_time_rate == 100.0


def test_sla_empty_result_returns_zero_rate(connection: sqlite3.Connection) -> None:
    result = sla_service.get_sla(connection, month="2099-01")

    assert result.items == []
    assert result.overall_on_time_rate == 0.0


def test_sla_endpoint_returns_200(client: TestClient) -> None:
    response = client.get("/api/v1/sla")

    assert response.status_code == 200
    assert response.json()["overall_on_time_rate"] == 66.67


def test_sla_endpoint_rejects_bad_month(client: TestClient) -> None:
    response = client.get("/api/v1/sla", params={"month": "2026/01"})

    assert response.status_code == 422
