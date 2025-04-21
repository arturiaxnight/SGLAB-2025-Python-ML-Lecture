# NTUH Python ML 分析課程 - 作業 1：Python 資料型態與操作 (解答)

---

## 第一部分：觀念題 (參考解答)

1.  **解釋 Python 中 可變 (mutable) 與 不可變 (immutable) 資料型態的差異，並各舉至少兩種例子。**

    *   **差異：**
        *   **不可變 (Immutable) 資料型態：** 一旦被創建，其值就不能被修改。如果嘗試對不可變物件進行修改，實際上會創建一個新的物件。
        *   **可變 (Mutable) 資料型態：** 創建後，其內容可以被修改，而不需要創建新的物件。修改是「原地 (in-place)」發生的。
    *   **例子：**
        *   **不可變 (Immutable)：** `int` (整數), `float` (浮點數), `str` (字串), `tuple` (元組), `bool` (布林值), `frozenset` (不可變集合)。
        *   **可變 (Mutable)：** `list` (列表), `dict` (字典), `set` (集合), `bytearray`。

2.  **`list.sort()` 方法和 `sorted(list)` 函數有何主要不同？請說明它們各自的使用時機。**

    *   **主要不同：**
        *   `list.sort()`：是列表物件的 **方法 (method)**。它會 **原地修改** 原來的列表，使其排序，並且 **返回 `None`**。
        *   `sorted(list)`：是一個 **內建函數 (built-in function)**。它會接收一個可迭代物件 (例如列表)，**返回一個新的已排序的列表**，而 **不改變** 原來的物件。
    *   **使用時機：**
        *   `list.sort()`：當你想要直接修改原始列表，並且不需要保留原始順序時使用。
        *   `sorted(list)`：當你需要一個排序後的列表副本，同時想要保留原始列表不變時，或者當你需要對任何可迭代物件 (不僅是列表，例如元組、字串、字典的鍵等) 進行排序並得到一個新的排序列表時使用。

3.  **為什麼 `list` 或 `dict` 不能直接作為字典 (`dict`) 的鍵 (key)？什麼樣的資料型態通常可以作為字典的鍵？**

    *   **原因：** 字典的鍵必須是 **可雜湊 (hashable)** 的。一個物件是可雜湊的，意味著它的值在生命週期內永不改變 (需要 `__hash__()` 方法)，並且可以與其他物件進行比較 (需要 `__eq__()` 方法)。因為 `list` 和 `dict` 是可變的，它們的內容可以改變，導致其雜湊值也會改變 (或者無法穩定計算)，因此它們不能作為字典的鍵。如果允許它們作鍵，那麼在修改列表或字典後，就可能無法再通過原來的鍵找到對應的值了。
    *   **可作為鍵的資料型態：** 通常是 **不可變 (immutable)** 的資料型態，例如 `int`, `float`, `str`, `tuple` (前提是元組內所有元素也都是不可變的), `bool`, `frozenset`。

4.  **`tuple` 和 `list` 的主要區別是什麼？在什麼情況下你會傾向於使用 `tuple` 而不是 `list`？**

    *   **主要區別：**
        *   `list` 是 **可變的 (mutable)**，可以新增、刪除或修改元素。
        *   `tuple` 是 **不可變的 (immutable)**，一旦創建就不能修改其內容。
    *   **傾向使用 `tuple` 的情況：**
        *   **表示固定集合：** 當你想表示一組不會改變的相關值時，例如座標 `(x, y)`、RGB 顏色值 `(r, g, b)`。
        *   **作為字典的鍵：** 因為元組是不可變的 (如果其元素也是不可變的)，所以可以用作字典的鍵。
        *   **保護資料不被意外修改：** 當你希望傳遞或存儲的序列資料不被函式或其他程式碼意外更改時。
        *   **異質資料結構：** 元組常用於表示結構化的、包含不同類型元素的記錄，而列表通常用於儲存同質性的元素序列。
        *   **效能考量 (微小)：** 在某些情況下，元組可能比列表佔用稍少的記憶體，且迭代速度可能稍快 (但差異通常不大，不應作為主要考量)。

5.  **解釋 Python 中的「淺拷貝」(shallow copy) 和「深拷貝」(deep copy) 的差異。在處理像 `[[1, 2], [3, 4]]` 這樣巢狀的列表時，這個差異為什麼很重要？**

    *   **差異：**
        *   **淺拷貝 (Shallow Copy)：** 創建一個新的物件，但如果原始物件包含對其他物件的引用 (例如巢狀列表中的子列表)，淺拷貝只會複製這些引用，而不是創建被引用物件的新副本。換句話說，新舊物件會共享內部的子物件。常用的方法有 `list.copy()`, `dict.copy()`, `[:]` 切片, `copy.copy()`。
        *   **深拷貝 (Deep Copy)：** 創建一個新的物件，並且 **遞迴地** 複製原始物件中包含的所有物件。這意味著即使是巢狀結構中的物件，也會被創建全新的副本，新舊物件完全獨立。需要使用 `copy` 模組的 `copy.deepcopy()` 函數。
    *   **重要性 (以 `nested_list = [[1, 2], [3, 4]]` 為例)：**
        *   如果對 `nested_list` 進行 **淺拷貝** 得到 `shallow_copy_list`，那麼 `nested_list` 和 `shallow_copy_list` 是兩個不同的列表物件。但是，它們內部的子列表 `[1, 2]` 和 `[3, 4]` 仍然是同一個物件的引用。如果你修改 `shallow_copy_list[0].append(99)`，那麼 `nested_list[0]` 也會變成 `[1, 2, 99]`，因為它們共享同一個子列表。
        *   如果對 `nested_list` 進行 **深拷貝** 得到 `deep_copy_list`，那麼不僅 `nested_list` 和 `deep_copy_list` 是不同的物件，它們內部的子列表 `[1, 2]` 和 `[3, 4]` 也會被完全複製成新的物件。如果你修改 `deep_copy_list[0].append(99)`，`nested_list[0]` 將保持不變 (`[1, 2]`)。
        *   因此，在處理巢狀結構時，如果你希望拷貝後的物件與原始物件完全獨立，互不影響，就必須使用深拷貝。如果只是想創建一個新的頂層容器，但共享內部元素，或者內部元素都是不可變的，那麼淺拷貝就足夠了。

---

## 第二部分：程式實作題 (參考解答)

```python
import copy # 用於深拷貝

# 1. 字串處理練習
print("--- 字串處理練習 ---")
s = "   NTUH Python ML Course 2025   "
print(f"原始字串: '{s}'")

# 移除字串前後的空白
s_stripped = s.strip()
print(f"移除空白後: '{s_stripped}'")

# 將整個字串轉換為小寫
s_lower = s_stripped.lower()
print(f"轉換小寫後: '{s_lower}'")

# 計算字元 'o' (小寫 o) 在處理過的字串中出現的次數
o_count = s_lower.count('o')
print(f"字元 'o' 出現次數: {o_count}")

# 檢查處理過的字串是否以 "ntuh" 開頭
starts_with_ntuh = s_lower.startswith("ntuh")
print(f"是否以 'ntuh' 開頭: {starts_with_ntuh}")

# 將字串中的 "ml" 替換為 "Machine Learning"
s_replaced = s_lower.replace("ml", "Machine Learning")
print(f"替換 'ml' 後: '{s_replaced}'")

# 使用 f-string 格式化輸出
# 從 s_replaced 中提取年份比較直接的方式是找到最後一個空格
last_space_index = s_replaced.rfind(' ')
course_name = s_replaced[:last_space_index]
year = s_replaced[last_space_index+1:]
# 或者直接用 s_lower 提取年份，因為替換不影響年份
# year = s_lower.split()[-1] # 另一種提取年份的方式
print(f"格式化輸出: Welcome to the {course_name} in {year}!")
print("-" * 20)

# 2. 列表操作練習
print("--- 列表操作練習 ---")
scores = [85, 92, 78, 92, 88, 75, 95]
print(f"原始列表: {scores}")

# 在列表末尾添加一個分數 100
scores.append(100)
print(f"添加 100 後: {scores}")

# 在索引 1 的位置插入分數 90
scores.insert(1, 90)
print(f"插入 90 到索引 1 後: {scores}")

# 移除第一個出現的分數 92
scores.remove(92)
print(f"移除第一個 92 後: {scores}")

# 找出分數 95 在列表中的索引位置，並印出該索引
index_95 = scores.index(95)
print(f"分數 95 的索引: {index_95}")

# 將列表 scores 按分數從高到低排序
scores.sort(reverse=True)
print(f"從高到低排序後: {scores}")

# 創建一個新列表 top_3_scores，包含排序後 scores 列表的前三個最高分
top_3_scores = scores[:3] # 使用切片
print(f"前三高分: {top_3_scores}")
print(f"排序操作後原始 scores 列表: {scores}") # 確認 scores 已被 sort 修改
print("-" * 20)

# 3. 字典應用練習
print("--- 字典應用練習 ---")
patient_record = {
    "name": "Mr. Lin",
    "age": 62,
    "conditions": ["Hypertension", "Hyperlipidemia"],
    "visit_date": "2025-04-20"
}
print(f"原始字典: {patient_record}")

# 新增一個鍵值對 "department": "Cardiology"
patient_record["department"] = "Cardiology"
print(f"新增科別後: {patient_record}")

# 更新 age 為 63
patient_record["age"] = 63
print(f"更新年齡後: {patient_record}")

# 將 "Hyperlipidemia" 從 conditions 列表中移除
if "Hyperlipidemia" in patient_record["conditions"]:
    patient_record["conditions"].remove("Hyperlipidemia")
print(f"移除 Hyperlipidemia 後: {patient_record}")

# 使用 .get() 方法嘗試獲取 "blood_type" 的值，如果不存在，則返回 "Unknown"
blood_type = patient_record.get("blood_type", "Unknown")
print(f"獲取血型 (get): {blood_type}")
print(f"原字典 (確認未修改): {patient_record}")

# 印出字典中所有的鍵 (keys)
print(f"所有鍵: {list(patient_record.keys())}") # 轉換為 list 以便清晰顯示

# 印出字典中所有的值 (values)
print(f"所有值: {list(patient_record.values())}") # 轉換為 list 以便清晰顯示
print("-" * 20)

# 4. 綜合應用練習
print("--- 綜合應用練習 ---")
records = [
    {"id": "A01", "diagnosis": "Pneumonia", "days_stay": 7},
    {"id": "B02", "diagnosis": "Fracture", "days_stay": 14},
    {"id": "C03", "diagnosis": "Pneumonia", "days_stay": 10},
    {"id": "D04", "diagnosis": "Appendicitis", "days_stay": 5}
]
print(f"原始記錄: {records}")

# 找出所有診斷為 "Pneumonia" 的病歷 id
pneumonia_ids = []
for record in records:
    if record["diagnosis"] == "Pneumonia":
        pneumonia_ids.append(record["id"])
# 列表推導式寫法: pneumonia_ids = [record["id"] for record in records if record["diagnosis"] == "Pneumonia"]
print(f"診斷為 Pneumonia 的 ID: {pneumonia_ids}")

# 計算所有病患的平均住院天數
total_days = 0
for record in records:
    total_days += record["days_stay"]
average_stay = total_days / len(records) if records else 0 # 避免除以零
# sum + 列表推導式寫法: total_days = sum(record["days_stay"] for record in records)
# average_stay = total_days / len(records) if records else 0
print(f"平均住院天數: {average_stay:.2f}") # 格式化為小數點後兩位

# 找出住院天數最長的病歷 id
longest_stay_id = None
max_days = -1 # 初始化為一個不可能的值
for record in records:
    if record["days_stay"] > max_days:
        max_days = record["days_stay"]
        longest_stay_id = record["id"]
# 使用 max 函數和 lambda 的寫法:
# longest_stay_record = max(records, key=lambda r: r["days_stay"]) if records else None
# longest_stay_id = longest_stay_record["id"] if longest_stay_record else None
print(f"住院最長的病歷 ID: {longest_stay_id}")
print("-" * 20)
