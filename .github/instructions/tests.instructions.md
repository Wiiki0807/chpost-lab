---
applyTo: "tests/**/*.py"
---

# 測試撰寫規範

- 一律使用 pytest 的 function style，不要用 `unittest.TestCase` class
- 使用 `tests/conftest.py` 既有的 `connection` 與 `client` fixture，不要自己建連線
- 測試名稱格式：`test_<行為>_<預期結果>`，用英文，要能單獨讀懂
- 一個測試只驗證一件事，避免一個 function 塞十個 assert
- 測試資料寫死在模組頂層常數（參考 `tests/test_region_stats.py` 的 `RECORDS`）
- 邊界情況要有：空輸入、被排除的狀態（`cancelled`）、超出門檻的時效
- API 測試要驗證 status code，錯誤參數要驗證回傳 422
- 不要 mock 掉正在測試的邏輯本身
