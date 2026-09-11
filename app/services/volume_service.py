from __future__ import annotations

import sqlite3

from app.models import MonthlyVolume, VolumeResponse
from app.repositories import volume_repository


def get_monthly_volume(
    connection: sqlite3.Connection,
    region: str | None = None,
    office_code: str | None = None,
) -> VolumeResponse:
    rows = volume_repository.monthly_volume(
        connection, region=region, office_code=office_code
    )
    items = [MonthlyVolume(**row) for row in rows]
    return VolumeResponse(
        items=items,
        total_pieces=sum(item.total_pieces for item in items),
    )
