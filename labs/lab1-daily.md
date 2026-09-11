# Lab 1：日常提效（7 分鐘動手）

## 目標

用 completions、inline chat 與正確的 context，修好一個 bug 並補上測試。

---

## 開發者路線

### 任務 A：修好跨月邊界 bug

`tests/test_delivery_service.py` 裡有一個失敗的測試。先跑它：

```powershell
pytest tests/test_delivery_service.py -k cross_month -v
```

失敗後，在 Chat 輸入：

```text
#terminalLastCommand 這個測試為什麼失敗？先解釋原因再給修法，不要直接改檔案。
```

**先問為什麼，再問怎麼改。** 直接叫它改，你會失去理解的機會。

理解原因後，再叫它改：

```text
#file:app/services/delivery_service.py 照你剛剛說的方式修正，只改必要的部分。
```

驗收：`pytest` 全綠。

### 任務 B：重構並補測試

開 `app/analytics/region_stats.py`，全選那個長函式，按 `Ctrl + I`：

```text
拆成數個職責單一的小函式，加上型別註記，保持對外行為完全不變。
```

接受 diff 後，再選取重構結果，在 Chat 輸入：

```text
#selection 為這些函式寫 pytest，參考 #file:tests/test_volume.py 的風格與 fixture 用法。
包含邊界情況：空資料、單筆資料、跨行政區。
```

**「參考既有測試的風格」這句話很重要。** 不加這句，它會自創一套風格。

驗收：新測試至少 3 個，`pytest` 全綠。

---

## 非撰碼路線（PM / QA / 架構師）

用 Chat 讀 codebase，產出一份「服務說明 + 風險點」。

```text
#codebase 請說明這個服務的資料流：從 HTTP request 進來到回傳 JSON，
中間經過哪些層、哪些檔案、哪些函式。用繁體中文，附上實際的檔名。
```

接著追問：

```text
根據你剛剛的分析，這個專案有哪三個最值得注意的技術風險？
每一點請指出具體的檔案或函式，不要泛泛而談。
```

把結果貼到共用頻道，等一下講評時會用到。

---

## 建議 prompt 對照

這張表是本 lab 的重點。**同樣的問題，差別只在 context。**

| 壞 prompt | 好 prompt | 差在哪 |
|---|---|---|
| `這個專案的時效怎麼算？` | `#codebase 這個專案的投遞時效是怎麼算的？請引用實際的檔案與函式名稱。` | 給了搜尋範圍，要求引用來源 |
| `幫我寫測試` | `#selection 為這些函式寫 pytest，參考 #file:tests/test_volume.py 的風格` | 指定了範圍與參考樣本 |
| `這裡有 bug 幫我修` | `#terminalLastCommand 這個測試為什麼失敗？先解釋原因再給修法` | 給了實際錯誤輸出，且先要理解 |

## 常用 context 語法

| 語法 | 作用 | 什麼時候用 |
|---|---|---|
| `#file` | 指定某個檔案 | 你知道答案在哪一檔 |
| `#selection` | 目前選取的程式碼 | 針對一段邏輯提問 |
| `#codebase` | 讓它搜尋整個 workspace | 你不知道在哪 |
| `#problems` | 目前的錯誤與警告 | 修編譯或 lint 錯誤 |
| `#terminalLastCommand` | 上一個終端機指令與輸出 | 測試或建置失敗 |

完整清單見 `labs/prompts-cheatsheet.md`。

## 觀看版重點

1. **Copilot 不會讀心。** 你覺得它笨的時候，九成是你沒給它該看的東西。
2. **Completions 的 context 是 docstring 與周圍的程式碼。** docstring 寫清楚，補全就準。
3. **要它模仿，就給它樣本。** 「參考 `tests/test_volume.py` 的風格」比「寫得好一點」有效一百倍。
4. **先問為什麼，再問怎麼改。** 這是你保有判斷力的關鍵。

## 卡住怎麼辦

| 問題 | 處置 |
|---|---|
| `#codebase` 回答很空泛 | workspace indexing 未完成，等一下再試 |
| Inline chat 的 diff 改壞了 | 按 Discard，重新選取範圍後再試一次，把需求講更具體 |
| 測試怎麼修都不過 | 別卡住，直接看講師的做法。下一個 lab 開始前執行 `git checkout lab-2-start` |
| 完全跟不上 | 專心看「context 對照」那段，那是本模組唯一必須帶走的東西 |
