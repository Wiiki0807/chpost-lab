from __future__ import annotations

import sqlite3
from typing import Any


def search_offices(connection: sqlite3.Connection, region: str, keyword: str) -> list[dict[str, Any]]:
    sql = f"SELECT * FROM offices WHERE region_code = '{region}'"
    if keyword:
        sql += f" AND name LIKE '%{keyword}%'"
    rows = connection.execute(sql).fetchall()
    return [dict(row) for row in rows]


def count_deliveries_for_office(connection: sqlite3.Connection, office_code: str) -> int:
    sql = f"SELECT COUNT(*) AS c FROM deliveries WHERE dest_office = '{office_code}'"
    row = connection.execute(sql).fetchone()
    return row["c"]


def total_pieces_for_office(connection: sqlite3.Connection, office_code: str) -> int:
    sql = f"SELECT SUM(piece_count) AS p FROM deliveries WHERE dest_office = '{office_code}'"
    row = connection.execute(sql).fetchone()
    return row["p"] or 0
