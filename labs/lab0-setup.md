# Lab 0：環境健檢（5 分鐘）

## 目標

確認你的 Copilot 能用、demo 專案能跑、Chat 讀得到 workspace。

## 步驟

### 1. 取得 demo 專案

在 GitHub 上開啟講師提供的 `chpost-lab` repo，點 **Use this template**
建立你自己的 repo，然後 clone 下來。

```powershell
git clone https://github.com/<你的帳號>/chpost-lab.git
cd chpost-lab
code .
```

離線備援：用講師提供的 `chpost-lab.zip` 解壓縮後開啟。

### 2. 確認 Copilot 已登入

看 VS Code 右下角狀態列的 Copilot 圖示：

- 正常：圖示為實心，滑鼠移上去顯示 `GitHub Copilot`
- 未登入：圖示有斜線，點它照指示登入

### 3. 安裝相依套件並跑測試

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

預期結果：大部分測試通過，`test_delivery_service.py` 裡有 **1 個失敗**。
這個失敗是刻意留的，Lab 1 會修它。

### 4. 產生資料庫

測試用的是記憶體資料庫，但要啟動服務得先產生真的資料檔：

```powershell
python scripts/seed_data.py
```

預期結果：`已寫入 52,272 筆投遞紀錄到 ...\data\postal.db`

> 這一步**不能跳過**。沒做的話下一步會出現 `no such table: deliveries`。

### 5. 啟動服務

```powershell
uvicorn app.main:app --reload
```

瀏覽器開 <http://localhost:8000/docs>，應該看到 Swagger UI，
裡面有一個可用的 `GET /api/v1/volume`。

### 6. 驗證 Chat 讀得到 workspace

開 Copilot Chat（`Ctrl + Alt + I`），輸入：

```text
#codebase 這個專案在做什麼？主要的資料流是什麼？
```

預期結果：它會提到 `deliveries`、`offices` 這些實際的表名，
以及 router / service / repository 的分層。

如果它給的是通用答案、沒有提到實際檔名，代表 workspace indexing 還沒完成，
等一分鐘再試一次。

## 觀看版重點

不動手也要記住這張表。**選錯介面是新手最常見的錯誤。**

| 介面 | 時間尺度 | 什麼時候用 |
|---|---|---|
| Completions | 秒 | 正在打字，知道自己要寫什麼 |
| Chat（Ask / Edit） | 分鐘 | 單檔到少量檔案，需要解釋或改寫 |
| Agent mode | 十分鐘 | 多檔、需要跑指令驗證的任務 |
| Copilot CLI | 十分鐘到自動化 | 終端機、腳本、CI |
| Cloud agent | 非同步 | 明確定義的任務，丟了就去做別的事 |
| Code review | 關卡 | PR 上的品質守門 |

兩條貫穿全場的觀念：

1. **context 決定品質。** 後面每個模組都在回答「怎麼給對 context」。
2. **人類保留 review 責任。** Copilot 產出的每一行都算你寫的。

## 卡住怎麼辦

| 問題 | 處置 |
|---|---|
| `pip install` 失敗 | 確認 Python 版本為 3.11 以上：`python --version` |
| Copilot 圖示一直轉 | 檢查公司網路是否擋了 `*.githubcopilot.com` |
| `pytest` 找不到模組 | 確認 venv 已啟用，且在專案根目錄執行 |
| 完全跑不起來 | 先別修，跟著看就好。Lab 1 開始前講師會給 checkpoint branch |
