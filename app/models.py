from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class DeliveryStatus(StrEnum):
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Delivery(BaseModel):
    id: int
    origin_office: str
    dest_office: str
    accepted_at: datetime
    delivered_at: datetime | None
    piece_count: int
    weight_g: int
    status: DeliveryStatus


class MonthlyVolume(BaseModel):
    month: str = Field(description="格式為 YYYY-MM")
    office_code: str
    office_name: str
    total_pieces: int


class VolumeResponse(BaseModel):
    items: list[MonthlyVolume]
    total_pieces: int
