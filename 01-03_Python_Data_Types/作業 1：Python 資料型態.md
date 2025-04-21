# NTUH Python ML 分析課程 - 作業 1：Python 資料型態與操作

**繳交期限：** [請自行設定日期]

**目標：** 熟悉 Python 的基本資料型態 (數字、字串、列表、字典、元組、集合、布林) 及其常用操作。

---

## 第一部分：觀念題 (請簡答)

1.  解釋 Python 中 **可變 (mutable)** 與 **不可變 (immutable)** 資料型態的差異，並各舉至少兩種例子。
2.  `list.sort()` 方法和 `sorted(list)` 函數有何主要不同？請說明它們各自的使用時機。
3.  為什麼 `list` 或 `dict` 不能直接作為字典 (`dict`) 的鍵 (key)？什麼樣的資料型態通常可以作為字典的鍵？
4.  `tuple` 和 `list` 的主要區別是什麼？在什麼情況下你會傾向於使用 `tuple` 而不是 `list`？
5.  解釋 Python 中的「淺拷貝」(shallow copy) 和「深拷貝」(deep copy) 的差異。在處理像 `[[1, 2], [3, 4]]` 這樣巢狀的列表時，這個差異為什麼很重要？

---

## 第二部分：程式實作題 (請撰寫 Python 程式碼完成)

1.  **字串處理練習:**
    *   給定一個字串 `s = "   NTUH Python ML Course 2025   "`。
    *   請完成以下操作，並印出每一步的結果：
        *   移除字串前後的空白。
        *   將整個字串轉換為小寫。
        *   計算字元 `'o'` (小寫 o) 在處理過的字串中出現的次數。
        *   檢查處理過的字串是否以 `"ntuh"` 開頭。
        *   將字串中的 `"ml"` 替換為 `"Machine Learning"`。
        *   使用 f-string，從處理過的字串中提取課程名稱 (`"ntuh python machine learning course"`) 和年份 (`"2025"`)，格式化輸出："Welcome to the [課程名稱] in [年份]!"。

2.  **列表操作練習:**
    *   創建一個列表 `scores = [85, 92, 78, 92, 88, 75, 95]`。
    *   請完成以下操作，並印出操作後的 `scores` 列表 (除非特別說明)：
        *   在列表末尾添加一個分數 `100`。
        *   在索引 `1` 的位置插入分數 `90`。
        *   移除第一個出現的分數 `92`。
        *   找出分數 `95` 在列表中的索引位置，並印出該索引。
        *   將列表 `scores` 按分數從高到低排序。
        *   創建一個新列表 `top_3_scores`，包含排序後 `scores` 列表的前三個最高分。印出 `top_3_scores`。

3.  **字典應用練習:**
    *   創建一個字典 `patient_record`，包含以下資訊：`"name": "Mr. Lin"`, `"age": 62`, `"conditions": ["Hypertension", "Hyperlipidemia"]`, `"visit_date": "2025-04-20"`。
    *   請完成以下操作，並印出操作後的 `patient_record` 字典：
        *   新增一個鍵值對 `"department": "Cardiology"`。
        *   更新 `age` 為 `63`。
        *   將 `"Hyperlipidemia"` 從 `conditions` 列表中移除。
        *   使用 `.get()` 方法嘗試獲取 `"blood_type"` 的值，如果不存在，則返回 `"Unknown"` 並印出結果 (不要修改原字典)。
        *   印出字典中所有的鍵 (keys)。
        *   印出字典中所有的值 (values)。

4.  **綜合應用練習:**
    *   給定一個包含多筆病歷摘要的列表 `records`：
        ```python
        records = [
            {"id": "A01", "diagnosis": "Pneumonia", "days_stay": 7},
            {"id": "B02", "diagnosis": "Fracture", "days_stay": 14},
            {"id": "C03", "diagnosis": "Pneumonia", "days_stay": 10},
            {"id": "D04", "diagnosis": "Appendicitis", "days_stay": 5}
        ]
        ```
    *   寫程式碼完成以下任務：
        *   找出所有診斷為 `"Pneumonia"` 的病歷 `id`，並存儲在一個新的列表 `pneumonia_ids` 中，最後印出此列表。
        *   計算所有病患的平均住院天數 (`days_stay`)，並印出結果。
        *   找出住院天數最長的病歷 `id`，並印出該 `id`。

---

## 第三部分：程式分析與除錯 (請回答問題或修改程式碼)

1.  **分析程式碼輸出：** 以下程式碼執行後，`list_x`, `list_y`, `list_z` 的最終內容會是什麼？請解釋為什麼。
    ```python
    list_x = [1, [2, 3]]
    list_y = list_x
    list_z = list_x.copy() # 淺拷貝

    list_y[0] = 10
    list_z[0] = 20
    list_y[1].append(4)
    list_z[1].append(5)

    print(f"list_x = {list_x}")
    print(f"list_y = {list_y}")
    print(f"list_z = {list_z}")
    ```

2.  **找出並修正錯誤：** 以下程式碼試圖修改元組中的元素，執行時會產生錯誤。請指出錯誤的原因，並說明如果想達到類似「修改」的效果 (例如得到 `(100, 2, 3)`)，應該如何做？
    ```python
    my_tuple = (1, 2, 3)
    # 嘗試修改元組 (會產生錯誤)
    my_tuple[0] = 100
    print(my_tuple)
    ```

3.  **預測輸出：** 執行以下程式碼，每一行 `print` 會輸出什麼？
    ```python
    text = "Data Science"
    print(text[2:6])
    print(text[::-2])
    print(text.find("Sci"))
    print(text.upper())
    print("data" in text.lower())
    ```

---