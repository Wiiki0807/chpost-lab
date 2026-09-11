# Prompt 與 Context 速查表

印出來放在鍵盤旁邊。

---

## Context 語法（Chat 裡用 `#` 叫出）

| 語法 | 作用 | 什麼時候用 |
|---|---|---|
| `#file:路徑` | 指定某個檔案 | 你知道答案在哪一檔 |
| `#selection` | 目前選取的程式碼 | 針對一段邏輯提問 |
| `#codebase` | 搜尋整個 workspace | 你不知道在哪 |
| `#problems` | 目前的錯誤與警告 | 修編譯或 lint 錯誤 |
| `#terminalLastCommand` | 上一個指令與輸出 | 測試或建置失敗 |
| `#changes` | 目前的 git 變更 | 請它 review 你的 diff |
| `#fetch:網址` | 抓取網頁內容 | 參考外部文件或規格 |

**隱性 context 也很重要：** 開著的編輯器 tab、游標位置、選取範圍，
Copilot 都會參考。要它專心，就關掉不相關的 tab。

---

## 快捷鍵

| 快捷鍵 | 功能 |
|---|---|
| `Ctrl + I` | Inline chat（在編輯器裡直接改） |
| `Ctrl + Alt + I` | 開啟 Chat 面板 |
| `Tab` | 接受整個補全 |
| `Ctrl + →` | 只接受一個詞 |
| `Alt + ]` / `Alt + [` | 下一個 / 上一個建議 |
| `Esc` | 拒絕補全 |

---

## 好 prompt 的四元素

寫給 agent 的需求，缺一個品質就明顯下降。

| 元素 | 範例句子 |
|---|---|
| **明確範圍** | `實作 GET /api/v1/sla，支援 region 與 month 參數` |
| **驗收條件** | `補上 pytest，並確保 pytest 全部通過` |
| **參考範例** | `照專案既有 /api/v1/volume 的三層寫法` |
| **禁止事項** | `不要修改資料庫 schema` |

---

## 常用句型

### 理解程式碼

```text
#codebase <問題>？請引用實際的檔案與函式名稱。
```

### 修 bug

```text
#terminalLastCommand 這個測試為什麼失敗？先解釋原因再給修法，不要直接改檔案。
```

### 生測試

```text
#selection 為這些函式寫測試，參考 #file:<既有測試檔> 的風格與 fixture 用法。
包含邊界情況：<列出來>。
```

### 重構

```text
拆成數個職責單一的小函式，加上型別註記，保持對外行為完全不變。
```

### 寫文件

```text
#codebase 幫我寫 <文件類型>，包含 <項目清單>。
不要寫你沒在程式碼裡看到的東西。
```

### 請它 review

```text
#changes review 我的變更，重點看安全性與效能問題。
每一條請說明為什麼，以及不改會有什麼後果。
```

---

## 反模式

| 不要這樣 | 改成這樣 |
|---|---|
| `幫我優化效能` | `#file:xxx.py 這個函式在 10 萬筆資料下很慢，找出瓶頸並提出改法` |
| `這裡有 bug` | `#terminalLastCommand 這個錯誤的根因是什麼？` |
| `寫得好一點` | `參考 #file:<範例> 的寫法改寫` |
| `幫我寫測試` | `#selection 寫 pytest，涵蓋空資料、單筆、跨區三種情況` |
| 一次要它做五件事 | 拆成五次，每次一件 |

---

## 客製化檔案位置

| 檔案 | 作用 |
|---|---|
| `.github/copilot-instructions.md` | 整個 repo 都生效 |
| `.github/instructions/*.instructions.md` | 用 `applyTo` 指定生效範圍 |
| `.github/prompts/*.prompt.md` | 用 `/檔名` 叫用 |
| `.github/agents/*.agent.md` | 自訂 agent |
| `AGENTS.md` | 跨工具通用的 agent 指引 |

改完 instructions 後，**要開新的 Chat session 才會生效**。

---

## 判斷訊號

| 訊號 | 意義 | 該做什麼 |
|---|---|---|
| 答案很通用、沒引用實際檔名 | 它沒讀到你的 code | 加 `#codebase` 或 `#file` |
| 它在同一處來回改第三次 | 它卡住了 | 停手，自己寫，或把任務拆更小 |
| 它改的檔案越來越多 | 需求太模糊 | 停止，重下 prompt，補上禁止事項 |
| 產出風格跟專案不一致 | 沒有共用規範 | 寫 `copilot-instructions.md` |
