from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(tags=["sla"])

# TODO: 實作 GET /api/v1/sla
# 回傳各投遞局的時效達成率，T+2 天內送達視為達標。
# 需支援 region 與 month 兩個 query 參數。
# 請照 volume.py 的三層寫法（router / service / repository）。
