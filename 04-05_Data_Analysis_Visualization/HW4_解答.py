import pandas as pd
import numpy as np

# Helper function to print section breaks
def section_break(title):
    print("\n" + "="*10 + f" {title} " + "="*10 + "\n")

# --- 題目一：創建 DataFrame 與基本操作 ---
section_break("題目一：創建 DataFrame 與基本操作")

# 1. 創建 DataFrame
patient_records_dict = {
    'patient_id': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'name': ['陳大明', '林小莉', '王曉華', '李建國', '吳美芳'],
    'diagnosis': ['高血壓', '糖尿病', '高血壓', '流感', '糖尿病'],
    'systolic_bp': [145, 130, 152, 120, 135]
}
patient_records = pd.DataFrame(patient_records_dict)
print("1. 創建的 patient_records DataFrame:")
print(patient_records)

# 2. 儲存與讀取 (概念)
#   說明如何將此 patient_records DataFrame 存為名為 patients.csv 的 CSV 檔案 (請勿包含索引)。
#   patient_records.to_csv('patients.csv', index=False)
print("\n2. 儲存與讀取 (概念):")
print("   - 將 DataFrame 存為 CSV (不含索引): patient_records.to_csv('patients.csv', index=False)")

#   說明如何從 patients.csv 讀取數據並將其載入到一個新的 DataFrame patients_from_csv 中，並顯示其前3筆記錄。
#   patients_from_csv = pd.read_csv('patients.csv')
#   print(patients_from_csv.head(3))
print("   - 從 CSV 讀取 DataFrame 並顯示前3筆: ")
print("     patients_from_csv = pd.read_csv('patients.csv')")
print("     print(patients_from_csv.head(3))")
# 實際操作 (假設已儲存並讀回，或直接用原 DataFrame 演示)
print("\n   (範例操作，使用原始 DataFrame):")
print(patient_records.head(3))


# --- 題目二：數據索引、選取與賦值 ---
section_break("題目二：數據索引、選取與賦值")
# 為了避免影響後續題目，這裡可以重新創建 patient_records 或複製
patient_records_q2 = patient_records.copy()
print("使用 patient_records DataFrame (或其副本):")
print(patient_records_q2)

# 1. 選取欄位
print("\n1. 選取欄位:")
name_and_bp = patient_records_q2[['name', 'systolic_bp']]
print("   - 'name' 和 'systolic_bp' 欄位:")
print(name_and_bp)

unique_diagnoses = patient_records_q2['diagnosis'].unique()
print("   - 'diagnosis' 欄位的唯一值:")
print(unique_diagnoses)

# 2. 條件選取 (loc/iloc)
print("\n2. 條件選取:")
bp_ge_140 = patient_records_q2.loc[patient_records_q2['systolic_bp'] >= 140]
print("   - systolic_bp >= 140 mmHg 的病患記錄:")
print(bp_ge_140)

selected_iloc = patient_records_q2.iloc[[0, 2, 4], patient_records_q2.columns.get_indexer(['patient_id', 'systolic_bp'])]
print("   - 使用 iloc 選取第 1, 3, 5 行的 'patient_id' 和 'systolic_bp':")
print(selected_iloc)

high_bp_records = patient_records_q2.loc[(patient_records_q2['diagnosis'] == '高血壓') & (patient_records_q2['systolic_bp'] > 150)]
print("   - diagnosis 為 '高血壓' 且 systolic_bp > 150 mmHg 的病患記錄:")
print(high_bp_records)

# 3. 賦值
print("\n3. 賦值:")
patient_records_q2.loc[patient_records_q2['patient_id'] == 'P003', 'systolic_bp'] = 148
print("   - 修改 P003 的 systolic_bp 為 148:")
print(patient_records_q2[patient_records_q2['patient_id'] == 'P003'])

patient_records_q2['needs_follow_up'] = patient_records_q2['systolic_bp'] > 140
print("   - 新增 'needs_follow_up' 欄位後:")
print(patient_records_q2)


# --- 題目三：摘要統計與數據轉換 ---
section_break("題目三：摘要統計與數據轉換")
patient_records_q3 = patient_records_q2.copy() # 使用上一題修改後的結果
print("使用 patient_records_q2 DataFrame (或其副本):")
print(patient_records_q3)

# 1. 描述性統計
print("\n1. 描述性統計 ('systolic_bp' 欄位):")
mean_bp = patient_records_q3['systolic_bp'].mean()
median_bp = patient_records_q3['systolic_bp'].median()
max_bp = patient_records_q3['systolic_bp'].max()
min_bp = patient_records_q3['systolic_bp'].min()
std_bp = patient_records_q3['systolic_bp'].std()
print(f"   - 平均值: {mean_bp}")
print(f"   - 中位數: {median_bp}")
print(f"   - 最高值: {max_bp}")
print(f"   - 最低值: {min_bp}")
print(f"   - 標準差: {std_bp:.2f}")

# 2. 數據轉換 (map/apply)
print("\n2. 數據轉換:")
def bp_to_level(bp):
    if bp >= 140:
        return '高血壓'
    elif bp >= 120:
        return '偏高'
    elif bp >= 90:
        return '正常'
    else:
        return '偏低'

patient_records_q3['bp_level'] = patient_records_q3['systolic_bp'].apply(bp_to_level)
print("   - 新增 'bp_level' 欄位後:")
print(patient_records_q3)


# --- 題目四：分組與排序 ---
section_break("題目四：分組與排序")

data_hospital_staff = {
    'staff_id': ['DR01', 'NR02', 'DR03', 'NR04', 'AD05', 'DR06', 'NR07'],
    'name': ['張醫師', '陳護理師', '王醫師', '李護理師', '周管理員', '吳醫師', '鄭護理師'],
    'department': ['內科', '外科', '內科', '外科', '行政部', '內科', '兒科'],
    'salary': [220000, 85000, 230000, 88000, 75000, 250000, 82000],
    'years_of_service': [10, 5, 12, 6, 3, 15, 4]
}
hospital_staff_df = pd.DataFrame(data_hospital_staff)
print("提供的 hospital_staff_df DataFrame:")
print(hospital_staff_df)

# 1. 分組計算
print("\n1. 分組計算:")
avg_salary_by_dept = hospital_staff_df.groupby('department')['salary'].mean()
print("   - 各部門平均 salary:")
print(avg_salary_by_dept)

dept_stats = hospital_staff_df.groupby('department').agg(
    staff_count=('staff_id', 'count'),
    total_years_of_service=('years_of_service', 'sum')
)
print("   - 各部門員工人數及總 years_of_service:")
print(dept_stats)

# 2. 排序
print("\n2. 排序:")
sorted_by_salary_desc = hospital_staff_df.sort_values(by='salary', ascending=False)
print("   - 按 salary 降序排序:")
print(sorted_by_salary_desc)

sorted_by_dept_and_years = hospital_staff_df.sort_values(by=['department', 'years_of_service'], ascending=[True, False])
print("   - 按 department 升序，再按 years_of_service 降序排序:")
print(sorted_by_dept_and_years)


# --- 題目五：處理缺失值與數據類型 ---
section_break("題目五：處理缺失值與數據類型")

data_lab_test_missing = {
    'test_id': ['T001', 'T002', 'T003', 'T004', 'T005', 'T006'],
    'test_name': ['血糖檢測', '血紅素', None, '膽固醇', '尿酸', '電解質'],
    'sample_volume_ml': [5, 2, 10, np.nan, 3, 4],
    'test_value': [100, 12.5, 200, 180, np.nan, 7.0]
}
lab_test_df_missing = pd.DataFrame(data_lab_test_missing)
print("提供的 lab_test_df_missing DataFrame:")
print(lab_test_df_missing)

# 1. 檢查缺失值
print("\n1. 檢查缺失值:")
missing_values = lab_test_df_missing.isnull().sum()
print("   - 每欄缺失值的數量:")
print(missing_values)

# 2. 填充缺失值
print("\n2. 填充缺失值:")
lab_test_df_filled = lab_test_df_missing.copy()
lab_test_df_filled['test_name'].fillna("未知檢測", inplace=True)
lab_test_df_filled['sample_volume_ml'].fillna(lab_test_df_filled['sample_volume_ml'].mean(), inplace=True)
lab_test_df_filled['test_value'].fillna(0, inplace=True)
print("   - 處理完缺失值後的 DataFrame:")
print(lab_test_df_filled)

# 3. 數據類型轉換
print("\n3. 數據類型轉換:")
# 確保 sample_volume_ml 是整數型態 (np.nan 在 mean() 後可能使欄位變 float)
lab_test_df_filled['sample_volume_ml'] = lab_test_df_filled['sample_volume_ml'].astype(int)
# test_value 應已是 float 或可轉為 float
lab_test_df_filled['test_value'] = lab_test_df_filled['test_value'].astype(float)
print("   - 轉換後 DataFrame 各欄位的數據類型:")
print(lab_test_df_filled.dtypes)


# --- 題目六：重命名與合併 DataFrame ---
section_break("題目六：重命名與合併 DataFrame")

# 1. 創建與重命名
print("\n1. 創建與重命名:")
df_appointments_data = {'appointment_id': ['AP01', 'AP02', 'AP03'], 'patient_id': ['P001', 'P002', 'P001']}
df_appointments = pd.DataFrame(df_appointments_data)
print("   - df_appointments:")
print(df_appointments)

df_patients_info_data = {'pat_id': ['P001', 'P002', 'P004'], 'patient_name': ['陳大明', '林小莉', '黃小強']}
df_patients_info = pd.DataFrame(df_patients_info_data)
print("   - df_patients_info (原始):")
print(df_patients_info)

df_patients_info_renamed = df_patients_info.rename(columns={'pat_id': 'patient_id'})
print("   - df_patients_info (重命名後):")
print(df_patients_info_renamed)

# 2. 合併 DataFrame
print("\n2. 合併 DataFrame:")
merged_inner = pd.merge(df_appointments, df_patients_info_renamed, on='patient_id', how='inner')
print("   - 內部合併 (inner merge):")
print(merged_inner)

merged_left = pd.merge(df_appointments, df_patients_info_renamed, on='patient_id', how='left')
print("   - 左合併 (left merge):")
print(merged_left)

section_break("Pandas 作業解答完畢") 