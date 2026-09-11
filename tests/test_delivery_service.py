from __future__ import annotations

from datetime import datetime

import pytest

from app.models import Delivery, DeliveryStatus
from app.services import delivery_service


def make_delivery(
    accepted: str,
    delivered: str | None,
    status: DeliveryStatus = DeliveryStatus.DELIVERED,
    dest: str = "800",
) -> Delivery:
    return Delivery(
        id=1,
        origin_office="100",
        dest_office=dest,
        accepted_at=datetime.fromisoformat(accepted),
        delivered_at=datetime.fromisoformat(delivered) if delivered else None,
        piece_count=10,
        weight_g=100,
        status=status,
    )


def test_transit_days_within_same_month() -> None:
    accepted = datetime.fromisoformat("2026-03-10 09:00:00")
    delivered = datetime.fromisoformat("2026-03-12 15:00:00")

    assert delivery_service.transit_days(accepted, delivered) == 2


def test_transit_days_across_month_boundary() -> None:
    accepted = datetime.fromisoformat("2026-01-31 09:00:00")
    delivered = datetime.fromisoformat("2026-02-02 15:00:00")

    assert delivery_service.transit_days(accepted, delivered) == 2


def test_is_on_time_for_cancelled_delivery() -> None:
    delivery = make_delivery("2026-03-10 09:00:00", None, DeliveryStatus.CANCELLED)

    assert delivery_service.is_on_time(delivery) is False


def test_average_transit_days_ignores_other_offices() -> None:
    deliveries = [
        make_delivery("2026-03-01 09:00:00", "2026-03-03 09:00:00", dest="800"),
        make_delivery("2026-03-01 09:00:00", "2026-03-05 09:00:00", dest="100"),
    ]

    assert delivery_service.average_transit_days(deliveries, "800") == 2.0


def test_average_transit_days_with_no_matching_delivery() -> None:
    assert delivery_service.average_transit_days([], "800") == 0.0


@pytest.mark.parametrize(
    ("accepted", "delivered", "expected"),
    [
        ("2026-03-10 09:00:00", "2026-03-11 09:00:00", True),
        ("2026-03-10 09:00:00", "2026-03-12 09:00:00", True),
        ("2026-03-10 09:00:00", "2026-03-14 09:00:00", False),
    ],
)
def test_is_on_time_threshold(accepted: str, delivered: str, expected: bool) -> None:
    delivery = make_delivery(accepted, delivered)

    assert delivery_service.is_on_time(delivery) is expected
