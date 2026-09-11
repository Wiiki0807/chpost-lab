from __future__ import annotations

import sqlite3

from fastapi import APIRouter, Depends, Query

from app.db import get_db
from app.models import VolumeResponse
from app.services import volume_service

router = APIRouter(tags=["volume"])


@router.get("/volume", response_model=VolumeResponse)
def get_volume(
    connection: sqlite3.Connection = Depends(get_db),
    region: str | None = Query(default=None, max_length=8, description="行政區代碼"),
    office_code: str | None = Query(default=None, max_length=8, description="局號"),
) -> VolumeResponse:
    """各局每月投遞量統計。"""
    return volume_service.get_monthly_volume(
        connection, region=region, office_code=office_code
    )
