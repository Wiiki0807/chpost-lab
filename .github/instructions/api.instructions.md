---
applyTo: "app/routers/**/*.py,app/repositories/**/*.py"
---

# API 與資料存取層規範

## Router 層

- 只做 HTTP 相關的事：參數宣告、驗證、回應模型；商業邏輯一律下放到 service
- 每個 query 參數都要有 `Query(...)` 並指定驗證條件與 `description`
  - 字串給 `max_length`，格式化字串給 `pattern`（例如月份 `^\d{4}-\d{2}$`）
- 一定要指定 `response_model`
- 用 `Depends(get_db)` 取得連線，不要在 router 裡自己開連線
- docstring 用繁體中文一句話說明這個端點做什麼

## Repository 層

- **只放 SQL 與參數綁定**，不做商業判斷
- SQL **必須使用 `?` 參數化查詢**。禁止 f-string、`%` 格式化、字串相加把使用者輸入拼進 SQL
- 動態條件的寫法：`sql += " AND col = ?"` 搭配 `params.append(value)`
- 回傳 `list[dict]`，用 `[dict(row) for row in rows]` 轉換
- 避免在迴圈裡逐筆查詢（N+1）；需要關聯資料請用 JOIN 一次查出來
