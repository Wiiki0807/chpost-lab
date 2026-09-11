from __future__ import annotations

from typing import Any


def calc(d: list[dict[str, Any]], r: str = "", t: int = 2, mode: str = "all") -> dict[str, Any]:
    res = {}
    tot = 0
    cnt = 0
    ok = 0
    byr = {}
    for i in d:
        if r != "" and i.get("region_code") != r:
            continue
        if i.get("status") == "cancelled":
            continue
        if mode == "delivered" and i.get("status") != "delivered":
            continue
        p = i.get("piece_count") or 0
        tot = tot + p
        cnt = cnt + 1
        td = i.get("transit_days")
        if td is not None and td <= t:
            ok = ok + 1
        rc = i.get("region_code") or "UNKNOWN"
        if rc not in byr:
            byr[rc] = {"pieces": 0, "count": 0, "ontime": 0}
        byr[rc]["pieces"] = byr[rc]["pieces"] + p
        byr[rc]["count"] = byr[rc]["count"] + 1
        if td is not None and td <= t:
            byr[rc]["ontime"] = byr[rc]["ontime"] + 1
    res["total_pieces"] = tot
    res["record_count"] = cnt
    if cnt > 0:
        res["on_time_rate"] = round(ok / cnt * 100, 2)
        res["avg_pieces"] = round(tot / cnt, 2)
    else:
        res["on_time_rate"] = 0
        res["avg_pieces"] = 0
    out = []
    for k in byr:
        v = byr[k]
        out.append(
            {
                "region_code": k,
                "total_pieces": v["pieces"],
                "record_count": v["count"],
                "on_time_rate": round(v["ontime"] / v["count"] * 100, 2) if v["count"] > 0 else 0,
            }
        )
    out.sort(key=lambda x: x["total_pieces"], reverse=True)
    res["by_region"] = out
    return res
