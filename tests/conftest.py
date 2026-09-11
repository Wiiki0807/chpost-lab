from __future__ import annotations

import sqlite3
from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from app.db import get_db, init_schema
from app.main import app

REGIONS = [("TPE", "臺北市"), ("KHH", "高雄市")]

OFFICES = [
    ("100", "臺北北門郵局", "TPE"),
    ("110", "臺北信義郵局", "TPE"),
    ("800", "高雄新興郵局", "KHH"),
]

# (origin, dest, accepted_at, delivered_at, piece_count, weight_g, status)
DELIVERIES = [
    ("100", "800", "2026-01-05 09:00:00", "2026-01-06 10:00:00", 100, 500, "delivered"),
    ("100", "800", "2026-01-20 09:00:00", "2026-01-24 10:00:00", 50, 800, "delivered"),
    ("110", "800", "2026-02-03 09:00:00", "2026-02-04 10:00:00", 80, 300, "delivered"),
    ("110", "100", "2026-02-10 09:00:00", None, 30, 200, "in_transit"),
    ("800", "100", "2026-02-14 09:00:00", None, 999, 100, "cancelled"),
]


@pytest.fixture()
def connection() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    init_schema(conn)
    conn.executemany("INSERT INTO regions (code, name) VALUES (?, ?)", REGIONS)
    conn.executemany(
        "INSERT INTO offices (code, name, region_code) VALUES (?, ?, ?)", OFFICES
    )
    conn.executemany(
        """INSERT INTO deliveries
           (origin_office, dest_office, accepted_at, delivered_at,
            piece_count, weight_g, status)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        DELIVERIES,
    )
    conn.commit()
    yield conn
    conn.close()


@pytest.fixture()
def client(connection: sqlite3.Connection) -> Iterator[TestClient]:
    app.dependency_overrides[get_db] = lambda: connection
    yield TestClient(app)
    app.dependency_overrides.clear()
