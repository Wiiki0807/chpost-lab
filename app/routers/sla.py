from __future__ import annotations

import sqlite3

from fastapi import APIRouter, Depends, Query

from app.db import get_db
from app.models import SlaResponse
from app.services import sla_service

router = APIRouter(tags=["sla"])


@router.get("/sla", response_model=SlaResponse)
def get_sla(
    connection: sqlite3.Connection = Depends(get_db),
    region: str | None = Query(default=None, max_length=8, description="行政區代碼"),
    month: str | None = Query(
        default=None, pattern=r"^\d{4}-\d{2}$", description="格式為 YYYY-MM"
    ),
) -> SlaResponse:
    """各投遞局時效達成率，T+2 天內送達視為達標。"""
    return sla_service.get_sla(connection, region=region, month=month)
