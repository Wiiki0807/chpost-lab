from __future__ import annotations

import sqlite3
from typing import Any

_SLA_SQL = """
    SELECT o.code AS office_code,
           o.name AS office_name,
           COUNT(*) AS delivered_count,
           SUM(
               CASE
                   WHEN CAST(julianday(DATE(d.delivered_at)) - julianday(DATE(d.accepted_at)) AS INTEGER) <= ?
                   THEN 1 ELSE 0
               END
           ) AS on_time_count
    FROM deliveries d
    JOIN offices o ON o.code = d.dest_office
    WHERE d.status = 'delivered'
      AND d.delivered_at IS NOT NULL
"""


def sla_by_office(
    connection: sqlite3.Connection,
    threshold_days: int,
    region: str | None = None,
    month: str | None = None,
) -> list[dict[str, Any]]:
    sql = _SLA_SQL
    params: list[Any] = [threshold_days]

    if region is not None:
        sql += " AND o.region_code = ?"
        params.append(region)
    if month is not None:
        sql += " AND strftime('%Y-%m', d.accepted_at) = ?"
        params.append(month)

    sql += " GROUP BY o.code, o.name ORDER BY o.code"

    rows = connection.execute(sql, params).fetchall()
    return [dict(row) for row in rows]
