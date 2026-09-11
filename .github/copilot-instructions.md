# chpost-lab 專案規範

## 專案是什麼

郵務數據平台，提供投遞量與時效（SLA）統計 API，外加一個單檔前端儀表板。
資料為程式產生的假造資料，無真實客戶資訊。

## 技術棧

- Python 3.11+、FastAPI、Pydantic v2
- SQLite（`data/postal.db`，由 `scripts/seed_data.py` 產生）
- pytest
- 前端：單檔 `dashboard.html` + Chart.js，**不要引入前端建置工具**

## 架構分層

一律遵守 router → service → repository 三層，不可跨層呼叫：

- `app/routers/` — 只處理 HTTP：參數驗證、回應模型，不放商業邏輯
- `app/services/` — 商業邏輯與計算，回傳 Pydantic 模型
- `app/repositories/` — 只放 SQL，回傳 `list[dict]`
- `app/models.py` — 所有 Pydantic 模型集中在此

**`volume` 那條線是標準範例。寫新功能時請照它的寫法。**

## 硬性規定

- SQL **一律使用參數化查詢**，禁止用 f-string 或字串相加拼接使用者輸入
- 所有 query 參數都要有驗證（`max_length`、`pattern`、`ge`/`le`）
- 公開函式要有型別註記與繁體中文 docstring
- 新增或修改商業邏輯時，**一定要同時補 pytest 測試**
- 測試用 `tests/conftest.py` 的 `connection` / `client` fixture，使用記憶體資料庫，不要碰真實 `data/postal.db`
- 不要為了讓測試通過而修改測試的預期值，先確認邏輯對不對

## 領域知識

- **時效達標定義**：收寄日到投遞日 T+2 天內（含）送達視為達標，常數在 `delivery_service.ON_TIME_THRESHOLD_DAYS`
- `status` 有三種：`in_transit`、`delivered`、`cancelled`
- 統計時 **`cancelled` 一律排除**；只有 `delivered` 且 `delivered_at` 非空才納入時效計算
- 局號（office code）為字串，不是數字，不要做數值比較或轉型
- 月份格式一律 `YYYY-MM`

## 命名慣例

- 函式與變數用 snake_case，語意要完整（`on_time_rate` 而非 `otr`、`r`）
- repository 函式命名為動作＋對象（`sla_by_office`、`monthly_volume`）
- 測試命名 `test_<行為>_<預期結果>`

## 回答方式

- 用**繁體中文**回答，技術名詞保留英文
- 回答要簡短直接，先講結論
- 修改程式碼時只動必要的部分，不要順手重構無關的程式碼
