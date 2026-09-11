"""產生可重現的假造投遞資料。執行：python scripts/seed_data.py"""

from __future__ import annotations

import random
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

# 讓腳本直接執行（python scripts/seed_data.py）時也找得到 app 套件
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.db import DB_PATH, connect, init_schema

RANDOM_SEED = 20260911
MONTHS_OF_HISTORY = 12

REGIONS = [
    ("TPE", "臺北市"),
    ("NTP", "新北市"),
    ("TXG", "臺中市"),
    ("KHH", "高雄市"),
    ("HUN", "花蓮縣"),
]

OFFICES = [
    ("100", "臺北北門郵局", "TPE"),
    ("104", "臺北中山郵局", "TPE"),
    ("110", "臺北信義郵局", "TPE"),
    ("220", "板橋郵局", "NTP"),
    ("231", "新店郵局", "NTP"),
    ("241", "三重郵局", "NTP"),
    ("400", "臺中民權路郵局", "TXG"),
    ("407", "臺中西屯郵局", "TXG"),
    ("800", "高雄新興郵局", "KHH"),
    ("806", "高雄前鎮郵局", "KHH"),
    ("970", "花蓮郵局", "HUN"),
    ("981", "玉里郵局", "HUN"),
]

# 旺季：農曆年前與雙十一，投遞量放大、時效變差
PEAK_MONTHS = {1, 11}
ANOMALY_OFFICE = "806"
ANOMALY_MONTH = 7


def _transit_days(rng: random.Random, month: int, is_peak_office: bool) -> int:
    if month in PEAK_MONTHS or is_peak_office:
        return rng.choices([1, 2, 3, 4, 5], weights=[10, 25, 30, 22, 13])[0]
    return rng.choices([1, 2, 3, 4, 5], weights=[35, 38, 17, 7, 3])[0]


def _piece_count(rng: random.Random, month: int, office_code: str) -> int:
    base = rng.randint(40, 180)
    if month in PEAK_MONTHS:
        base = int(base * 1.8)
    if office_code == ANOMALY_OFFICE and month == ANOMALY_MONTH:
        base = int(base * 3.5)
    return base


def generate_rows(seed: int = RANDOM_SEED) -> list[tuple]:
    rng = random.Random(seed)
    end = date.today().replace(day=1)
    start = end - timedelta(days=MONTHS_OF_HISTORY * 31)
    start = start.replace(day=1)

    rows: list[tuple] = []
    current = start
    while current < end:
        for origin, _, _ in OFFICES:
            for dest, _, _ in OFFICES:
                if origin == dest:
                    continue
                accepted = datetime.combine(
                    current, datetime.min.time()
                ) + timedelta(hours=rng.randint(8, 18))

                status = rng.choices(
                    ["delivered", "in_transit", "cancelled"],
                    weights=[94, 4, 2],
                )[0]

                is_peak_office = origin == ANOMALY_OFFICE and current.month == ANOMALY_MONTH
                if status == "delivered":
                    days = _transit_days(rng, current.month, is_peak_office)
                    delivered = (accepted + timedelta(days=days)).isoformat(sep=" ")
                else:
                    delivered = None

                rows.append(
                    (
                        origin,
                        dest,
                        accepted.isoformat(sep=" "),
                        delivered,
                        _piece_count(rng, current.month, origin),
                        rng.randint(50, 20000),
                        status,
                    )
                )
        current += timedelta(days=1)
    return rows


def main() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()

    connection = connect()
    try:
        init_schema(connection)
        connection.executemany("INSERT INTO regions (code, name) VALUES (?, ?)", REGIONS)
        connection.executemany(
            "INSERT INTO offices (code, name, region_code) VALUES (?, ?, ?)", OFFICES
        )

        rows = generate_rows()
        connection.executemany(
            """INSERT INTO deliveries
               (origin_office, dest_office, accepted_at, delivered_at,
                piece_count, weight_g, status)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            rows,
        )
        connection.commit()
        print(f"已寫入 {len(rows):,} 筆投遞紀錄到 {DB_PATH}")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
