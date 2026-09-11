from __future__ import annotations

import sqlite3
from typing import Any

_MONTHLY_VOLUME_SQL = """
    SELECT strftime('%Y-%m', d.accepted_at) AS month,
           o.code                           AS office_code,
           o.name                           AS office_name,
           SUM(d.piece_count)               AS total_pieces
    FROM deliveries d
    JOIN offices o ON o.code = d.origin_office
    WHERE d.status != 'cancelled'
"""


def monthly_volume(
    connection: sqlite3.Connection,
    region: str | None = None,
    office_code: str | None = None,
) -> list[dict[str, Any]]:
    sql = _MONTHLY_VOLUME_SQL
    params: list[Any] = []

    if region is not None:
        sql += " AND o.region_code = ?"
        params.append(region)
    if office_code is not None:
        sql += " AND o.code = ?"
        params.append(office_code)

    sql += " GROUP BY month, o.code, o.name ORDER BY month, o.code"

    rows = connection.execute(sql, params).fetchall()
    return [dict(row) for row in rows]


def list_deliveries(
    connection: sqlite3.Connection,
    dest_office: str | None = None,
    month: str | None = None,
) -> list[dict[str, Any]]:
    sql = "SELECT * FROM deliveries WHERE 1 = 1"
    params: list[Any] = []

    if dest_office is not None:
        sql += " AND dest_office = ?"
        params.append(dest_office)
    if month is not None:
        sql += " AND strftime('%Y-%m', accepted_at) = ?"
        params.append(month)

    rows = connection.execute(sql, params).fetchall()
    return [dict(row) for row in rows]
