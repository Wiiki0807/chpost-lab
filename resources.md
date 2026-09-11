# 資源與後續學習路徑

---

## 今天用到的官方文件

### 核心概念

| 主題 | 連結 |
|---|---|
| Copilot 概念總覽 | <https://docs.github.com/en/copilot/concepts> |
| Completions 運作原理 | <https://docs.github.com/en/copilot/concepts/completions> |
| Copilot Chat | <https://docs.github.com/en/copilot/concepts/chat> |
| Prompting 概念 | <https://docs.github.com/en/copilot/concepts/prompting> |
| Context 概念 | <https://docs.github.com/en/copilot/concepts/context> |
| Agents 概念 | <https://docs.github.com/en/copilot/concepts/agents> |
| AI 模型選擇 | <https://docs.github.com/en/copilot/concepts/models> |

### 操作指南

| 主題 | 連結 |
|---|---|
| How-tos 總覽 | <https://docs.github.com/en/copilot/how-tos> |
| 取得程式碼建議 | <https://docs.github.com/en/copilot/how-tos/get-code-suggestions> |
| 使用 Copilot Chat | <https://docs.github.com/en/copilot/how-tos/chat-with-copilot> |
| 提供 context | <https://docs.github.com/en/copilot/how-tos/provide-context> |
| 設定 custom instructions | <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions-in-your-ide> |
| 使用 Copilot agents | <https://docs.github.com/en/copilot/how-tos/use-copilot-agents> |
| Copilot CLI | <https://docs.github.com/en/copilot/how-tos/copilot-cli> |
| 在 GitHub 上使用 Copilot | <https://docs.github.com/en/copilot/how-tos/copilot-on-github> |

### 團隊與治理

| 主題 | 連結 |
|---|---|
| Copilot code review | <https://docs.github.com/en/copilot/concepts/agents/code-review> |
| Cloud agent | <https://docs.github.com/en/copilot/concepts/agents/cloud-agent> |
| Agent skills | <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills> |
| Agentic Workflows | <https://docs.github.com/en/copilot/concepts/agents/about-github-agentic-workflows> |
| 使用量數據 | <https://docs.github.com/en/copilot/concepts/copilot-usage-metrics> |
| Content exclusion | <https://docs.github.com/en/copilot/how-tos/configure-content-exclusion> |
| 團隊管理 | <https://docs.github.com/en/copilot/how-tos/administer-copilot> |
| 企業概念 | <https://docs.github.com/en/copilot/concepts/enterprise> |

---

## 建議的後續學習路徑

### 第一週：把今天的東西用起來

1. 在你**真正的工作專案**建立 `.github/copilot-instructions.md`
2. 連續五天，每天至少用一次 agent mode 完成一個真實任務
3. 記錄哪些 prompt 有效、哪些沒用

**這一週的目標不是學新東西，是把習慣建立起來。**

### 第二到四週：累積團隊資產

1. 把團隊最常做的三個動作寫成 prompt files
2. 用 `applyTo` 為測試、API、前端分別寫路徑範圍 instructions
3. 在 PR 流程加入 Copilot code review
4. 試著把一個真實的 issue 指派給 cloud agent

### 第二個月：自動化與擴充

1. 把 Copilot CLI 放進一個 CI 步驟（例如自動檢查 PR 描述品質）
2. 評估要不要接 MCP server（GitHub MCP 最實用）
3. 把團隊的領域知識封裝成 skill
4. 看一次 usage metrics，找出需要協助的同事

---

## 今天的教材

| 檔案 | 內容 |
|---|---|
| `labs/prompts-cheatsheet.md` | Prompt 與 context 語法速查，建議印出來 |
| `labs/lab0-setup.md` ~ `lab5-challenge.md` | 完整的操作步驟，可自行重跑 |
| `plan.md` | 整體規劃，想自己辦內訓可以參考 |
| `agenda.md` | 講師腳本，含每個 demo 的完整 prompt |

---

## 三句話總結今天

1. **選對介面。** 六種介面對應六種時間尺度，選錯會事倍功半。
2. **給對 context。** 你覺得它笨的時候，九成是你沒給它該看的東西。
3. **保留 review 責任。** Copilot 產出的每一行都算你寫的。

---

## 有問題怎麼辦

- 官方文件：<https://docs.github.com/en/copilot>
- 官方社群討論：<https://github.com/orgs/community/discussions/categories/copilot>
- 內部：聯絡講師或你的 GitHub 管理員
