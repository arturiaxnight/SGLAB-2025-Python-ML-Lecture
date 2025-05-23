#%% 作業 5：乳癌資料集視覺化分析 - 解答範本

#%% 載入必要套件
from sklearn.datasets import load_breast_cancer # 修改載入的資料集
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from matplotlib.lines import Line2D # 用於自訂圖例

#%% 任務 1：載入與初步探索資料
print("--- 任務 1：載入與初步探索資料 ---")
# 1. 載入資料集
cancer_data = load_breast_cancer() # 修改資料集變數名稱
X = cancer_data.data
y = cancer_data.target
feature_names = cancer_data.feature_names
target_names = cancer_data.target_names

# 2. 轉換為 Pandas DataFrame
df_cancer = pd.DataFrame(X, columns=feature_names) # 修改 DataFrame 名稱
df_cancer['diagnosis'] = pd.Categorical.from_codes(y, target_names) # 修改目標欄位名稱

# 3. 印出前五筆記錄
print("\n--- First 5 records ---")
print(df_cancer.head())

# 4. 印出基本資訊
print("\n--- Basic Info ---")
df_cancer.info()

# 5. 印出資料集描述 (部分)
print("\n--- Dataset Description (Partial) ---")
print(cancer_data.DESCR.split('\n\n')[0]) 
print(cancer_data.DESCR.split('\n\n')[1]) # 印出更多描述資訊

# 6. 印出各類別樣本數
print("\n--- Samples per class ---")
print(df_cancer['diagnosis'].value_counts())
print("-------------------------------------\n")

#%% 任務 2：使用 Matplotlib 進行視覺化
print("--- 任務 2：使用 Matplotlib 進行視覺化 ---")
sns.set_theme(style="whitegrid")

# 1. 散佈圖
plt.figure(figsize=(10, 6))
feature1_mpl = 'mean radius' # 建議的醫學相關特徵
feature2_mpl = 'mean texture' # 建議的醫學相關特徵

scatter_mpl = plt.scatter(df_cancer[feature1_mpl], df_cancer[feature2_mpl], c=y, cmap='viridis', edgecolor='k')
plt.xlabel(feature1_mpl)
plt.ylabel(feature2_mpl)
plt.title(f'Matplotlib: {feature1_mpl} vs {feature2_mpl} by Diagnosis') # 更新標題
handles_mpl, _ = scatter_mpl.legend_elements()
plt.legend(handles_mpl, target_names, title="Diagnosis") # 更新圖例標題
plt.grid(True)
plt.show()

# 2. 盒鬚圖
features_for_boxplot_mpl = ['mean perimeter', 'mean area', 'mean smoothness'] # 建議的醫學相關特徵
plt.figure(figsize=(18, 6))
for i, feature in enumerate(features_for_boxplot_mpl):
    plt.subplot(1, len(features_for_boxplot_mpl), i + 1)
    data_to_plot = [df_cancer[df_cancer['diagnosis'] == target_name][feature] for target_name in target_names]
    plt.boxplot(data_to_plot, labels=target_names, patch_artist=True)
    plt.title(f'Matplotlib: {feature} Distribution by Diagnosis') # 更新標題
    plt.ylabel(feature)
    plt.xlabel("Diagnosis") # 更新 X 軸標籤
plt.tight_layout()
plt.show()
print("-------------------------------------\n")

#%% 任務 3：使用 Seaborn 進行視覺化
print("--- 任務 3：使用 Seaborn 進行視覺化 ---")

# 1. Seaborn 散佈圖
feature1_sns = 'mean radius' # 與 Matplotlib 範例相同
feature2_sns = 'mean texture' # 與 Matplotlib 範例相同
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_cancer, x=feature1_sns, y=feature2_sns, hue='diagnosis', palette='viridis', s=70, edgecolor='k') # 更新 hue 欄位
plt.title(f'Seaborn: {feature1_sns} vs {feature2_sns} by Diagnosis') # 更新標題
plt.show()

# 2. 小提琴圖
feature_for_violin_sns = 'mean compactness' # 建議的醫學相關特徵
plt.figure(figsize=(8, 6))
sns.violinplot(data=df_cancer, x='diagnosis', y=feature_for_violin_sns, palette='pastel') # 更新 x 欄位
plt.title(f'Seaborn: {feature_for_violin_sns} Distribution by Diagnosis') # 更新標題
plt.xlabel("Diagnosis") # 更新 X 軸標籤
plt.ylabel(feature_for_violin_sns)
plt.show()

# 3. 相關係數熱力圖
plt.figure(figsize=(20, 18)) # 可能需要更大的圖來顯示所有特徵
correlation_matrix = df_cancer.drop('diagnosis', axis=1).corr()
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, annot_kws={"size": 7})
plt.title('Seaborn: Correlation Matrix of Breast Cancer Features') # 更新標題
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
print("-------------------------------------\n")

#%% 任務 4 (進階挑戰)：視覺化模型預測結果
print("--- 任務 4 (進階挑戰)：視覺化模型預測結果 ---")

# 1. 資料準備與模型訓練
feature_for_model_1 = 'worst radius' # 建議的醫學相關特徵
feature_for_model_2 = 'worst concave points' # 建議的醫學相關特徵
X_model = df_cancer[[feature_for_model_1, feature_for_model_2]]
y_model = y

# 標準化
scaler = StandardScaler()
X_model_scaled = scaler.fit_transform(X_model)

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X_model_scaled, y_model, test_size=0.3, random_state=42, stratify=y_model)

# 訓練模型
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# 2. 預測與混淆矩陣視覺化
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n--- Model Performance ({feature_for_model_1} & {feature_for_model_2}) ---")
print(f"Accuracy: {acc:.2f}")

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=target_names, yticklabels=target_names)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title(f'Confusion Matrix for Breast Cancer (Accuracy: {acc:.2f})') # 更新標題
plt.show()

# 3. (可選) 預測結果散佈圖
df_test_results = pd.DataFrame(X_test, columns=[feature_for_model_1, feature_for_model_2])
df_test_results['true_class_code'] = y_test
df_test_results['predicted_class_code'] = y_pred
df_test_results['correct_prediction'] = (df_test_results['true_class_code'] == df_test_results['predicted_class_code'])
df_test_results['true_class_name'] = pd.Categorical.from_codes(df_test_results['true_class_code'], target_names)

plt.figure(figsize=(12, 8))
scatter_preds = sns.scatterplot(
    data=df_test_results, 
    x=feature_for_model_1, 
    y=feature_for_model_2, 
    hue='true_class_name',
    style='correct_prediction',
    palette='viridis', 
    s=100,
    edgecolor='k'
)

plt.xlabel(f"Standardized {feature_for_model_1}")
plt.ylabel(f"Standardized {feature_for_model_2}")
plt.title(f'Model Predictions on Breast Cancer Test Set ({feature_for_model_1} & {feature_for_model_2})') # 更新標題

handles, labels = scatter_preds.get_legend_handles_labels()
num_hue_levels = len(target_names)

new_labels = labels[:num_hue_levels]
style_labels_orig = labels[num_hue_levels+1:] 

new_style_labels = []
for sl in style_labels_orig:
    if sl == 'True':
        new_style_labels.append('Correctly Classified')
    elif sl == 'False':
        new_style_labels.append('Misclassified')
    else:
        new_style_labels.append(sl)

plt.legend(handles[:num_hue_levels] + handles[num_hue_levels+1:], 
           new_labels + new_style_labels, 
           title="Diagnosis / Prediction") # 更新圖例標題
plt.grid(True)
plt.show()
print("-------------------------------------\n")

print("作業範本結束。請基於此範本完成您的作業。") 