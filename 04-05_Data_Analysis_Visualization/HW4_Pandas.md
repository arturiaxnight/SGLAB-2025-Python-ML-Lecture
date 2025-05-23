# Pandas 作業：數據分析與操作練習

請根據課堂所學的 Pandas 知識，完成以下練習。建議您在 Jupyter Notebook 或 Python 環境中實際操作。

**檔案準備：**

在開始之前，請確保您已經安裝了 Pandas 套件。
```python
import pandas as pd
import numpy as np # numpy 可能在處理缺失值或創建範例數據時用到
```

---

## 題目一：創建 DataFrame 與基本操作

1.  **創建 DataFrame:**
    *   請使用一個 Python 字典創建一個名為 `patient_records` 的 DataFrame。
    *   此 DataFrame 應包含以下欄位：
        *   `patient_id`: ['P001', 'P002', 'P003', 'P004', 'P005']
        *   `name`: ['陳大明', '林小莉', '王曉華', '李建國', '吳美芳']
        *   `diagnosis`: ['高血壓', '糖尿病', '高血壓', '流感', '糖尿病']
        *   `systolic_bp`: [145, 130, 152, 120, 135]  (收縮壓)
    *   印出創建的 DataFrame。

2.  **儲存與讀取 (概念):**
    *   說明如何將此 `patient_records` DataFrame 存為名為 `patients.csv` 的 CSV 檔案 (請勿包含索引)。
    *   說明如何從 `patients.csv` 讀取數據並將其載入到一個新的 DataFrame `patients_from_csv` 中，並顯示其前3筆記錄。(在解答中，您可以假設檔案已成功儲存並接著讀取，或者直接操作 `patient_records` 並註解說明實際讀取步驟)

---

## 題目二：數據索引、選取與賦值

延續題目一創建的 `patient_records` DataFrame (或重新創建一個相似的 DataFrame 進行操作)：

1.  **選取欄位:**
    *   選取並印出 `name` 和 `systolic_bp` 這兩欄。
    *   選取並印出 `diagnosis` 欄位的所有唯一值。

2.  **條件選取 (loc/iloc):**
    *   選取所有 `systolic_bp` 大于等于 140 mmHg 的病患記錄，並印出。
    *   使用 `iloc` 選取 DataFrame 中的第 1、3、5 行 (索引為 0, 2, 4) 的 `patient_id` 和 `systolic_bp` 欄位，並印出。
    *   選取 `diagnosis` 為 '高血壓' 且 `systolic_bp` 高於 150 mmHg 的病患記錄。

3.  **賦值:**
    *   將 `patient_id` 為 'P003' 的病患的 `systolic_bp` 修改為 148。
    *   新增一個名為 `needs_follow_up` 的欄位，對於 `systolic_bp` 高於 140 mmHg 的病患，此欄位值設為 `True`，否則設為 `False`。印出修改後的 DataFrame。

---

## 題目三：摘要統計與數據轉換

延續題目二修改後的 `patient_records` DataFrame：

1.  **描述性統計:**
    *   計算 `systolic_bp` 欄位的平均值、中位數、最高值、最低值以及標準差。

2.  **數據轉換 (map/apply):**
    *   新增一個名為 `bp_level` 的欄位。使用 `apply` 或 `map` 方法，根據以下規則轉換 `systolic_bp`：
        *   140 mmHg 及以上: '高血壓'
        *   120-139 mmHg: '偏高'
        *   90-119 mmHg: '正常'
        *   90 mmHg 以下: '偏低'
    *   印出包含 `bp_level` 的 DataFrame。

---

## 題目四：分組與排序

使用以下提供的 `hospital_staff_data` DataFrame 進行操作：

```python
data = {
    'staff_id': ['DR01', 'NR02', 'DR03', 'NR04', 'AD05', 'DR06', 'NR07'],
    'name': ['張醫師', '陳護理師', '王醫師', '李護理師', '周管理員', '吳醫師', '鄭護理師'],
    'department': ['內科', '外科', '內科', '外科', '行政部', '內科', '兒科'],
    'salary': [220000, 85000, 230000, 88000, 75000, 250000, 82000],
    'years_of_service': [10, 5, 12, 6, 3, 15, 4]
}
hospital_staff_df = pd.DataFrame(data)
```

1.  **分組計算:**
    *   按 `department` 分組，計算每個部門的平均 `salary`。
    *   按 `department` 分組，計算每個部門的員工人數以及總 `years_of_service`。

2.  **排序:**
    *   將 `hospital_staff_df` 按照 `salary` 欄位進行降序排序，印出結果。
    *   將 `hospital_staff_df` 先按 `department` 升序排序，再按 `years_of_service` 降序排序，印出結果。

---

## 題目五：處理缺失值與數據類型

使用以下包含缺失值的 `lab_test_data` DataFrame：

```python
data_missing = {
    'test_id': ['T001', 'T002', 'T003', 'T004', 'T005', 'T006'],
    'test_name': ['血糖檢測', '血紅素', None, '膽固醇', '尿酸', '電解質'],
    'sample_volume_ml': [5, 2, 10, np.nan, 3, 4],
    'test_value': [100, 12.5, 200, 180, np.nan, 7.0] # 假設為檢測數值
}
lab_test_df_missing = pd.DataFrame(data_missing)
```

1.  **檢查缺失值:**
    *   檢查 `lab_test_df_missing` 中每一欄是否有缺失值，並計算每欄缺失值的數量。

2.  **填充缺失值:**
    *   將 `test_name` 欄位的缺失值填充為 "未知檢測"。
    *   將 `sample_volume_ml` 欄位的缺失值用該欄位的平均數填充。
    *   將 `test_value` 欄位的缺失值用 0 填充。
    *   印出處理完缺失值後的 DataFrame。

3.  **數據類型轉換:**
    *   (假設) 填充完缺失值後，確保 `sample_volume_ml` 欄位是整數型態 (int)。
    *   將 `test_value` 欄位轉換為浮點數型態 (float)，如果它還不是。
    *   印出轉換後 DataFrame 各欄位的數據類型。

---

## 題目六：重命名與合併 DataFrame

1.  **創建與重命名:**
    *   創建兩個 DataFrame：
        *   `df_appointments`: 包含 `appointment_id` (AP01, AP02, AP03) 和 `patient_id` (P001, P002, P001)。
        *   `df_patients_info`: 包含 `pat_id` (P001, P002, P004) 和 `patient_name` (陳大明, 林小莉, 黃小強)。
    *   將 `df_patients_info` 中的 `pat_id` 欄位重命名為 `patient_id` 以便於合併。

2.  **合併 DataFrame:**
    *   使用 `patient_id` 作為共同鍵，將 `df_appointments` 和 `df_patients_info` 進行內部合併 (inner merge)，得到一個包含預約資訊以及對應病患名稱的新 DataFrame。印出合併結果。
    *   使用 `patient_id` 作為共同鍵，將 `df_appointments` 和 `df_patients_info` 進行左合併 (left merge)，確保所有預約都被保留。印出合併結果。

---

祝您練習愉快！ 