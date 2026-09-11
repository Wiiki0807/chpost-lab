# Lab 4：團隊協作與自動化（8 分鐘動手）

## 目標

體驗三種「離開 IDE」的 Copilot：PR 上的 code review、非同步的 cloud agent、終端機裡的 CLI。

---

## 必做：請 Copilot review 你的 PR

### 步驟 1：把 Lab 2 的成果推上去

```powershell
git checkout -b feat/sla-endpoint
git add -A
git commit -m "feat: 加上 SLA 時效達成率端點"
git push -u origin feat/sla-endpoint
```

### 步驟 2：開 PR 並指派 Copilot

1. 到 GitHub.com 上你的 repo，點 **Compare & pull request**
2. 建立 PR
3. 右側 **Reviewers** 選 **Copilot**
4. 等它產出 review（通常 30 秒到 2 分鐘）

### 步驟 3：看它抓到什麼

逐條讀它的留言。重點看：

- 它抓到的是**明顯的問題**（安全性、效能、邊界情況），還是雞毛蒜皮？
- 有沒有誤報？
- 哪一條你會直接採納，哪一條你會反駁？

### 步驟 4：互動

- 挑一條建議按 **Apply suggestion** 一鍵套用
- 在另一條留言下追問：`為什麼這樣比較好？有什麼取捨？`

**要帶走的觀念：它不會取代 code review，它會把明顯的問題先清掉，
讓人類 reviewer 專注在設計與商業邏輯上。**

---

## 選做：Copilot CLI

### 安裝

```powershell
npm install -g @github/copilot
```

### 啟動並問問題

```powershell
copilot
```

在互動模式裡問：

```text
這個 repo 的測試怎麼跑？有哪些測試目前是失敗的？
```

### 讓它做實際的事

```text
幫我產生過去 12 個月每月的投遞量統計，輸出成 reports/monthly.csv
```

### 看一眼 programmatic 模式

```powershell
copilot -p "檢查這個 repo 是否有硬編碼的密鑰" --allow-all-tools
```

**這一行可以放進 CI。這是從「工具」變成「基礎設施」的分界點。**

---

## 觀察：Cloud agent（講師示範，不用跟做）

講師在 Lab 0 的時候就把一個 issue 指派給 Copilot 了。現在回去看結果：

- 它自己開了 branch
- 它自己 commit
- 它開了一個 draft PR
- PR 描述裡有它的推理過程與 session log

**這是今天最大的心態轉變：你不是在等它寫完，你是去開會，回來 review。**

如果你想自己試（時間夠的話）：

1. 在你的 repo 開一個 issue，描述一個小功能
2. 在 Assignees 選 Copilot
3. 去做別的事，等它開 PR

---

## 非撰碼路線（PM / QA / 架構師）

**寫一個好 issue，讓 cloud agent 能直接接手。**

好 issue 的公式跟好 prompt 一樣，就是那四個元素：

```markdown
## 需求
<一句話講清楚要什麼>

## 驗收條件
- [ ] <可驗證的條件 1>
- [ ] <可驗證的條件 2>
- [ ] 所有測試通過

## 參考
請照 `<某個既有檔案>` 的既有寫法。

## 不要做
- <明確的禁止事項>
```

寫完後指派給 Copilot，觀察它的產出品質。

**這個練習的結論：寫得清楚的 issue，AI 跟人類工程師都做得比較好。**

---

## 觀看版重點

記住這條時間軸：

```text
即時（IDE）→ 非同步（cloud agent）→ 自動（workflow）
   分鐘級          小時級             不需要你在場
```

三個要點：

1. **Code review 是品質關卡，不是取代人。** 它清掉噪音，你專注在設計。
2. **Cloud agent 改變的是工作節奏，不是速度。** 價值在於你可以同時做別的事。
3. **CLI 的真正價值在於可以進 CI。** 互動模式只是開胃菜。

## 卡住怎麼辦

| 問題 | 處置 |
|---|---|
| Reviewers 裡沒有 Copilot 選項 | 你的 org 可能未啟用，看講師示範即可 |
| push 被拒絕 | 確認 remote 是你自己的 repo，不是講師的 |
| CLI 安裝失敗 | 需要 Node.js 18 以上。裝不起來就跳過，看講師示範 |
| Cloud agent 沒反應 | 正常，它可能要 10 分鐘以上。看講師的截圖即可 |
