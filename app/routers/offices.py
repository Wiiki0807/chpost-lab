from __future__ import annotations

import sqlite3
from typing import Any

from fastapi import APIRouter, Depends

from app.db import get_db
from app.services import office_service

router = APIRouter(tags=["offices"])


@router.get("/offices")
def search_offices(
    region: str,
    keyword: str = "",
    connection: sqlite3.Connection = Depends(get_db),
) -> list[dict[str, Any]]:
    return office_service.search(connection, region, keyword)
