from __future__ import annotations

import sqlite3

from app.models import OfficeSla, SlaResponse
from app.repositories import sla_repository
from app.services.delivery_service import ON_TIME_THRESHOLD_DAYS


def get_sla(
    connection: sqlite3.Connection,
    region: str | None = None,
    month: str | None = None,
) -> SlaResponse:
    rows = sla_repository.sla_by_office(
        connection,
        threshold_days=ON_TIME_THRESHOLD_DAYS,
        region=region,
        month=month,
    )

    items = [
        OfficeSla(
            office_code=row["office_code"],
            office_name=row["office_name"],
            delivered_count=row["delivered_count"],
            on_time_count=row["on_time_count"],
            on_time_rate=_rate(row["on_time_count"], row["delivered_count"]),
        )
        for row in rows
    ]

    total_delivered = sum(item.delivered_count for item in items)
    total_on_time = sum(item.on_time_count for item in items)

    return SlaResponse(
        items=items,
        overall_on_time_rate=_rate(total_on_time, total_delivered),
    )


def _rate(on_time: int, total: int) -> float:
    if total == 0:
        return 0.0
    return round(on_time / total * 100, 2)
