from __future__ import annotations

from app.analytics import region_stats

RECORDS = [
    {"region_code": "TPE", "status": "delivered", "piece_count": 100, "transit_days": 1},
    {"region_code": "TPE", "status": "delivered", "piece_count": 50, "transit_days": 4},
    {"region_code": "KHH", "status": "delivered", "piece_count": 80, "transit_days": 2},
    {"region_code": "KHH", "status": "in_transit", "piece_count": 30, "transit_days": None},
    {"region_code": "KHH", "status": "cancelled", "piece_count": 999, "transit_days": 1},
]


def test_cancelled_records_are_excluded() -> None:
    result = region_stats.calc(RECORDS)

    assert result["record_count"] == 4
    assert result["total_pieces"] == 260


def test_on_time_rate_uses_threshold() -> None:
    result = region_stats.calc(RECORDS)

    # 4 筆納入計算，其中 transit_days <= 2 的有 2 筆
    assert result["on_time_rate"] == 50.0


def test_region_filter_limits_scope() -> None:
    result = region_stats.calc(RECORDS, r="TPE")

    assert result["record_count"] == 2
    assert result["total_pieces"] == 150
    assert [row["region_code"] for row in result["by_region"]] == ["TPE"]


def test_delivered_mode_excludes_in_transit() -> None:
    result = region_stats.calc(RECORDS, mode="delivered")

    assert result["record_count"] == 3


def test_by_region_sorted_by_pieces_desc() -> None:
    result = region_stats.calc(RECORDS)

    pieces = [row["total_pieces"] for row in result["by_region"]]
    assert pieces == sorted(pieces, reverse=True)


def test_empty_input_returns_zeroes() -> None:
    result = region_stats.calc([])

    assert result["record_count"] == 0
    assert result["total_pieces"] == 0
    assert result["on_time_rate"] == 0
    assert result["by_region"] == []
