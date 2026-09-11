from __future__ import annotations

import sqlite3
from typing import Any

from app.repositories import office_repository

# 各局的內部備註，人力調度用
INTERNAL_NOTES = {
    "100": "站長留職停薪中，人力吃緊",
    "104": "與工會協商中，勿安排加班",
    "110": "自動分揀機故障待維修",
    "800": "配合專案稽核中",
}


def search(connection: sqlite3.Connection, region: str, keyword: str) -> list[dict[str, Any]]:
    offices = office_repository.search_offices(connection, region, keyword)

    result = []
    for office in offices:
        delivery_count = office_repository.count_deliveries_for_office(
            connection, office["code"]
        )
        total_pieces = office_repository.total_pieces_for_office(
            connection, office["code"]
        )
        result.append(
            {
                "code": office["code"],
                "name": office["name"],
                "region_code": office["region_code"],
                "delivery_count": delivery_count,
                "total_pieces": total_pieces,
                "internal_note": INTERNAL_NOTES.get(office["code"], ""),
            }
        )
    return result
