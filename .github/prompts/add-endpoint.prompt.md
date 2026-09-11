---
mode: agent
description: 依照專案三層架構新增一個統計 API 端點，含測試
---

# 新增統計端點

請新增一個 API 端點。如果我沒有講清楚以下資訊，先問我再動手：

- 端點路徑與要回答的商業問題
- 需要哪些 query 參數
- 回傳欄位

## 實作要求

照 `volume` 那條線的三層寫法，依序建立或修改：

1. `app/models.py` — 新增 request/response 的 Pydantic 模型
2. `app/repositories/<name>_repository.py` — 只放 SQL，參數化查詢，回傳 `list[dict]`
3. `app/services/<name>_service.py` — 商業邏輯，回傳 Pydantic 模型
4. `app/routers/<name>.py` — HTTP 層，指定 `response_model`，參數要有驗證
5. `app/main.py` — 用 `app.include_router(..., prefix="/api/v1")` 註冊
6. `tests/test_<name>.py` — 用既有 fixture 撰寫測試

## 驗收條件

- `pytest` 全數通過
- 新端點在 <http://localhost:8000/docs> 看得到且可試打
- 統計一律排除 `cancelled`；時效計算只納入 `delivered` 且 `delivered_at` 非空的紀錄
- 沒有任何字串拼接的 SQL

完成後請列出你改了哪些檔案，以及你做了哪些我沒有指定的決定。
