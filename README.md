# chpost-lab — GitHub Copilot Workshop 練習專案

一個**郵務數據平台**，用來在 3 小時的 GitHub Copilot workshop 裡當作練習場。

專案裡刻意留了幾個缺口（一個壞掉的函式、一個沒實作的端點、缺少的文件），
每個缺口都對應一個 lab。你會用 Copilot 把它們一個一個補起來。

---

## 快速開始

```powershell
# 1. 建立虛擬環境並安裝套件
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 2. 產生資料庫（約 5 萬筆假造投遞紀錄）
python scripts/seed_data.py

# 3. 跑測試
pytest

# 4. 啟動服務
uvicorn app.main:app --reload
```

瀏覽器開 <http://localhost:8000/docs> 看 Swagger UI。

> **`pytest` 會有 1 個失敗是正常的。** 那是刻意留給 Lab 1 的題目。
> 預期結果：**12 passed, 1 failed**。

儀表板：啟動服務後直接用瀏覽器開啟 `dashboard.html`。

---

## 專案結構

```
app/
├── main.py                  FastAPI 進入點
├── db.py                    SQLite 連線與 schema
├── models.py                Pydantic 模型
├── routers/
│   ├── volume.py            ✅ 完整範例，照這個寫法模仿
│   └── sla.py               ⬜ 空殼（Lab 2 的題目）
├── services/
│   ├── volume_service.py    ✅ 完整範例
│   └── delivery_service.py  🐛 有一個 bug（Lab 1 的題目）
├── repositories/
│   └── volume_repository.py ✅ 完整範例
└── analytics/
    └── region_stats.py      ♻️ 沒測試、命名很糟（Lab 1 的題目）

scripts/seed_data.py         產生假造資料
tests/                       pytest 測試
dashboard.html               前端儀表板
labs/                        👉 練習手冊在這裡
```

**`volume` 那條線（router → service → repository）是完整的。**
當你要 Copilot 寫新東西時，叫它參考這條線的寫法，品質會好很多。

---

## 資料模型

| 表 | 說明 |
|---|---|
| `regions` | 行政區（TPE 臺北市、KHH 高雄市…） |
| `offices` | 郵局據點（局號、名稱、所屬行政區） |
| `deliveries` | 投遞紀錄（收寄局、投遞局、收寄/投遞時間、件數、重量、狀態） |

時效定義：**T+2 天內送達視為達標**。

---

## 練習手冊

| Lab | 主題 |
|---|---|
| [Lab 0](labs/lab0-setup.md) | 環境健檢 |
| [Lab 1](labs/lab1-daily.md) | 日常提效：補全、Chat、測試、重構、debug |
| [Lab 2](labs/lab2-agent.md) | Agent 模式：端到端完成 SLA 端點 |
| [Lab 3](labs/lab3-customize.md) | 客製化：instructions、prompt files、custom agents |
| [Lab 4](labs/lab4-team.md) | 團隊協作：code review、cloud agent、CLI |
| [Lab 5](labs/lab5-challenge.md) | 綜合挑戰 |
| [速查表](labs/prompts-cheatsheet.md) | Prompt 與 context 語法 |

事前準備請看 [setup/prerequisites.md](setup/prerequisites.md)。
延伸資源請看 [resources.md](resources.md)。

---

## 跟不上怎麼辦

每個 lab 都有對應的起始點 branch，直接跳到下一關：

```powershell
git checkout lab-2-start   # 直接取得 Lab 1 已完成的狀態
```

| Branch | 狀態 |
|---|---|
| `lab-1-start` | 原始狀態 |
| `lab-2-start` | Lab 1 已完成（bug 修好、測試補齊） |
| `lab-3-start` | Lab 2 已完成（SLA 端點做好） |
| `lab-4-start` | Lab 3 已完成（instructions 寫好） |

---

## 說明

資料全為程式產生的假造資料，與中華郵政或任何真實組織無關，僅供教學使用。
