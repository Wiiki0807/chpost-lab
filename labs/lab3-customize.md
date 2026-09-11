# Lab 3：客製化（7 分鐘動手）

## 目標

寫出一份能讓 Copilot 真的照你的專案規範做事的 custom instructions。
這是**今天投資報酬率最高的一件事**。

---

## 客製化的四層

依投資報酬率排序。大多數團隊做完第一層就有八成的收益。

| 層級 | 檔案 | 作用範圍 | 花費時間 |
|---|---|---|---|
| 1. Repository instructions | `.github/copilot-instructions.md` | 整個 repo 的每一次對話 | 10 分鐘 |
| 2. 路徑範圍 instructions | `.github/instructions/*.instructions.md` | 符合 `applyTo` 的檔案 | 5 分鐘 |
| 3. Prompt files | `.github/prompts/*.prompt.md` | 你主動叫用時 | 10 分鐘 |
| 4. Custom agents / Skills | `.github/agents/`、skills | 特定任務 | 30 分鐘以上 |

MCP 排在最後。**先把 instructions 寫好再玩 MCP，順序不要反。**

---

## 必做：第一層 Repository instructions

### 步驟 1：先做「前」的對照

開一個新的 Chat，輸入：

```text
幫我加一個 GET /api/v1/offices 端點，列出所有郵局據點。
```

**不要接受它的建議。** 把結果留在畫面上，觀察：

- 有沒有照三層架構？
- SQL 是字串拼接還是參數化？
- 有沒有附測試？
- 用什麼語言回答？

### 步驟 2：建立 instructions

建立 `.github/copilot-instructions.md`，填入下面的模板：

```markdown
# chpost-lab 專案規範

## 技術棧
Python 3.11、FastAPI、SQLite、pandas、pytest。

## 架構
API 一律分三層：router 只處理 HTTP，service 放商業邏輯，repository 負責資料存取。
router 不可直接碰資料庫。

## 強制規則
- SQL 一律使用參數化查詢，禁止字串拼接
- 所有對外端點都要有 Pydantic 輸入驗證
- 新增或修改 service 一定要附 pytest
- 公開函式必須有型別註記

## 回答方式
用繁體中文回答，技術名詞保留英文。
```

### 步驟 3：做「後」的對照

**開一個全新的 Chat**（重要，舊的 session 不會重讀），下一模一樣的 prompt。

並排比較兩次的結果。差異應該非常明顯。

---

## 選做：第三層 Prompt file

把「新增端點」這個團隊標準動作變成一個指令。

建立 `.github/prompts/new-endpoint.prompt.md`：

```markdown
---
mode: agent
description: 依專案規範新增一個 API 端點
---

請新增一個 API 端點。我會告訴你端點名稱與需求。

做這些事：
1. 在 `app/routers/` 新增 router，只處理 HTTP 與輸入驗證
2. 在 `app/services/` 新增 service，放商業邏輯
3. 需要查資料時在 `app/repositories/` 新增方法，使用參數化查詢
4. 在 `tests/` 新增 pytest，至少涵蓋正常路徑與一個邊界情況
5. 跑 pytest 確認全綠

參考 `app/routers/volume.py` 的既有寫法。
```

在 Chat 輸入 `/new-endpoint` 叫用它。

**prompt file 的價值：新人到職第一天就能照著做對。**

---

## 非撰碼路線（PM / QA / 架構師）

為你**自己團隊**寫一份 instructions 草稿。不需要懂 code，需要懂團隊規範。

用這個填空模板：

```markdown
# <你的團隊或專案名稱> 規範

## 我們在做什麼
<一到兩句話講清楚這個系統的用途>

## 技術棧
<語言、框架、資料庫>

## 架構慣例
<分層方式、資料夾結構、命名慣例>

## 絕對不要做的事
<列出踩過的坑，例如：不要直接改 production 設定檔>

## 測試要求
<用什麼測試框架、什麼情況一定要有測試>

## 回答方式
用繁體中文回答，技術名詞保留英文。
```

寫「絕對不要做的事」時，**回想你們團隊過去踩過的坑**。這一段通常最有價值。

---

## 觀看版重點

1. **instructions 是一次性投資，每次對話都受益。** 花 10 分鐘寫，團隊一整年受用。
2. **`applyTo` 讓規範只在該生效的地方生效。** 不要把所有規則塞進同一個檔案。
3. **改完 instructions 要開新的 Chat 才會生效。**
4. **當你發現自己一直在對話裡重複貼同一段背景知識，就該把它變成 skill。**
5. **順序：instructions → prompt files → custom agents → MCP。** 不要跳級。

## 卡住怎麼辦

| 問題 | 處置 |
|---|---|
| 建了檔案但看不出差別 | 確認開的是**新的** Chat session |
| 不知道該寫什麼規則 | 從「我最常糾正 Copilot 的三件事」開始寫 |
| `/new-endpoint` 叫不出來 | 確認檔名結尾是 `.prompt.md`，且放在 `.github/prompts/` |
| MCP 連不上 | 直接跳過，不要現場 debug。概念聽懂就好 |
