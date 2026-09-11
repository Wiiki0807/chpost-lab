from __future__ import annotations

from datetime import datetime

from app.models import Delivery, DeliveryStatus

ON_TIME_THRESHOLD_DAYS = 2


def transit_days(accepted_at: datetime, delivered_at: datetime) -> int:
    """回傳從收寄到投遞所經過的天數。"""
    return (delivered_at - accepted_at).days


def is_on_time(delivery: Delivery) -> bool:
    """判斷單筆投遞是否在 T+2 內送達。未送達或已取消一律視為未達標。"""
    if delivery.status != DeliveryStatus.DELIVERED or delivery.delivered_at is None:
        return False
    return transit_days(delivery.accepted_at, delivery.delivered_at) <= ON_TIME_THRESHOLD_DAYS


def average_transit_days(deliveries: list[Delivery], office_code: str) -> float:
    """計算指定投遞局的平均時效天數，排除已取消與尚未送達的件。"""
    completed = [
        d
        for d in deliveries
        if d.dest_office == office_code
        and d.status == DeliveryStatus.DELIVERED
        and d.delivered_at is not None
    ]
    if not completed:
        return 0.0

    total = sum(transit_days(d.accepted_at, d.delivered_at) for d in completed)  # type: ignore[arg-type]
    return round(total / len(completed), 2)
