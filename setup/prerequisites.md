# 學員前置作業

> **請在 workshop 開始前完成。** 全部做完大約 20 分鐘。
> 現場網路會很擠，當天才裝來不及。

---

## 檢查清單

完成後請逐項打勾。

- [ ] 1. GitHub 帳號可登入，且已啟用 Copilot
- [ ] 2. VS Code 安裝完成（1.95 以上）
- [ ] 3. GitHub Copilot 擴充套件安裝並登入
- [ ] 4. Python 3.11 以上
- [ ] 5. Git 可用
- [ ] 6. 網域白名單確認
- [ ] 7. 選配：Node.js（給 Copilot CLI 用）

---

## 1. GitHub 帳號與 Copilot 授權

開啟 <https://github.com/settings/copilot>。

看到 **Copilot is active** 或方案名稱，代表正常。
若顯示未啟用，請聯絡貴公司的 GitHub 管理員。

---

## 2. VS Code

下載：<https://code.visualstudio.com/>

確認版本：`說明` → `關於`，版本需為 **1.95** 以上。

---

## 3. GitHub Copilot 擴充套件

在 VS Code 的擴充套件面板搜尋並安裝：

- **GitHub Copilot**
- **GitHub Copilot Chat**

安裝後，點右下角狀態列的 Copilot 圖示登入。

**驗證方式：** 新開一個 `.py` 檔案，打一行註解 `# 計算兩數相加`，
按 Enter 後應該會出現灰色的建議文字。

---

## 4. Python 3.11 以上

```powershell
python --version
```

若版本低於 3.11 或找不到 python，從 <https://www.python.org/downloads/> 安裝。

**Windows 安裝時記得勾選 `Add Python to PATH`。**

建議一併安裝 VS Code 的 **Python** 擴充套件。

---

## 5. Git

```powershell
git --version
```

若找不到，從 <https://git-scm.com/downloads> 安裝。

---

## 6. 網域白名單

如果你在公司網路後面，請確認這些網域沒有被擋：

```text
github.com
api.github.com
copilot-proxy.githubusercontent.com
*.githubcopilot.com
default.exp-tas.com
```

**快速測試：** 在 VS Code 開任何檔案，看 Copilot 圖示是否正常（不是斜線、不是一直轉圈）。

如果被擋，當天請坐在能用手機熱點的位置。

---

## 7. 選配：Node.js（Copilot CLI 用）

只有 Lab 4 的選做部分需要。沒裝也能完成 workshop 的必做內容。

```powershell
node --version
```

需要 18 以上。安裝後：

```powershell
npm install -g @github/copilot
copilot --version
```

---

## 當天要帶的東西

- 筆電（充飽電，帶變壓器）
- 能上網的手機（萬一公司網路擋 Copilot 的備案）
- 外接螢幕不必，但建議把 VS Code 字級調大一點，方便和講師畫面對照

---

## 完成後的自我驗證

在 VS Code 開一個空資料夾，開啟 Copilot Chat（`Ctrl + Alt + I`），輸入：

```text
你好，請用繁體中文回答：你現在能讀到我的 workspace 嗎？
```

有回應就代表一切正常。

---

## 遇到問題

| 問題 | 處置 |
|---|---|
| Copilot 圖示一直轉圈 | 網路被擋，見第 6 節 |
| 登入後又跳出登入 | 清除 VS Code 的 GitHub 認證後重登 |
| Copilot 沒有建議出現 | 確認檔案有存成 `.py` 等已知副檔名 |
| 公司電腦不能裝軟體 | 提前告知講師，當天以觀看為主 |

實在解決不了不要緊，**workshop 設計成「跟不上也能學到東西」**，
每個 lab 都有觀看版重點。
