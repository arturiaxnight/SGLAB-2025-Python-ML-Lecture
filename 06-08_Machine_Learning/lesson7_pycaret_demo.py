# %%
"""
Lesson 7: PyCaret AutoML 自動化機器學習實際操作練習
=======================================================

本範例介紹如何使用 PyCaret 進行自動化機器學習，包含分類與回歸任務
PyCaret 是一個低代碼的機器學習庫，可以大幅簡化 ML 工作流程

pip install pycaret[full]
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg') # 設定 Matplotlib 後端為非互動式，避免 GUI 錯誤
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer, load_diabetes
import warnings
warnings.filterwarnings('ignore')

# matplotlib 和 seaborn 設定
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 10
sns.set_style("whitegrid")  # 設定 seaborn 樣式
sns.set_palette("husl")     # 設定色彩調色板

print("=" * 60)
print("Lesson 7: PyCaret AutoML 自動化機器學習實際操作練習")
print("=" * 60)

# %%
# ============================================================================
# Part 1: PyCaret 分類任務 (Classification) - 使用乳腺癌資料集
# ============================================================================

print("\n🎗️ Part 1: 分類任務 - 乳腺癌資料集")
print("-" * 50)

# 載入乳腺癌資料集
cancer = load_breast_cancer()
cancer_df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
cancer_df['target'] = cancer.target

print(f"資料形狀: {cancer_df.shape}")
print(f"分類標籤: {cancer.target_names}")
print("\n前5筆資料:")
print(cancer_df.head())

# 檢查目標變數分布
print(f"\n目標變數分布:")
print(cancer_df['target'].value_counts().sort_index())

# %%
# 基本資料視覺化 - 使用 seaborn
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# 準備目標變數標籤
cancer_df['diagnosis'] = cancer_df['target'].map({0: 'malignant', 1: 'benign'})

# 1. 目標變數分布
sns.countplot(data=cancer_df, x='diagnosis', ax=axes[0, 0])
axes[0, 0].set_title('Breast Cancer Diagnosis Distribution')
axes[0, 0].set_xlabel('Diagnosis')
axes[0, 0].set_ylabel('Count')

# 2. 重要特徵的分布
important_features = ['mean radius', 'mean texture', 'mean perimeter', 'mean area']
for i, feature in enumerate(important_features[:4]):
    row = (i + 1) // 3
    col = (i + 1) % 3
    sns.histplot(data=cancer_df, x=feature, hue='diagnosis', alpha=0.7, ax=axes[row, col])
    axes[row, col].set_title(f'{feature.title()} Distribution')
    axes[row, col].set_xlabel(feature.title())

# 移除多餘的子圖
if len(important_features) < 5:
    axes[1, 2].remove()

plt.tight_layout()
plt.savefig('part1_data_visualization.png')
print("\nℹ️  Part 1 資料視覺化圖表已儲存至 'part1_data_visualization.png'")
plt.close() # 關閉圖表以釋放資源

# %%
# 開始 PyCaret 分類任務
print("\n🚀 開始 PyCaret 分類工作流程...")

import pycaret.classification as pc

# 1. 設定實驗環境
print("\n1️⃣ 設定實驗環境...")
clf_exp = pc.setup(data=cancer_df, 
                    target='target', 
                    session_id=123,
                    train_size=0.8)

print("✅ 實驗環境設定完成")

# 2. 比較多種模型
print("\n2️⃣ 比較多種分類模型...")
best_models = pc.compare_models(
    include=['lr', 'rf', 'et', 'nb', 'svm', 'knn'],
    sort='Accuracy',
    n_select=3,
    verbose=False
)

print("✅ 模型比較完成，已選出最佳的3個模型")

# 3. 創建最佳模型
print("\n3️⃣ 創建最佳模型...")
best_model = pc.create_model('rf')  # Random Forest
print("✅ Random Forest 模型創建完成")

# 4. 調整超參數
print("\n4️⃣ 調整超參數...")
tuned_model = pc.tune_model(best_model, optimize='Accuracy')
print("✅ 超參數調整完成")

# 5. 評估模型
print("\n5️⃣ 評估調整後的模型...")
pc.evaluate_model(tuned_model)

# 6. 預測測試集
print("\n6️⃣ 預測測試集...")
predictions = pc.predict_model(tuned_model)
print("✅ 測試集預測完成")
print(f"預測結果形狀: {predictions.shape}")

# 7. 完成最終模型
print("\n7️⃣ 完成最終模型...")
final_model = pc.finalize_model(tuned_model)
print("✅ 最終模型完成")

# 8. 部署準備
print("\n8️⃣ 保存模型...")
pc.save_model(final_model, 'breast_cancer_classification_model')
print("✅ 模型已保存為 'breast_cancer_classification_model.pkl'")


# %%
# ============================================================================
# Part 2: PyCaret 回歸任務 (Regression) - 使用糖尿病資料集
# ============================================================================

print("\n\n📊 Part 2: 回歸任務 - 糖尿病資料集")
print("-" * 50)

# 載入糖尿病資料集
diabetes = load_diabetes()
diabetes_df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
diabetes_df['target'] = diabetes.target

print(f"資料形狀: {diabetes_df.shape}")
print("\n前5筆資料:")
print(diabetes_df.head())

# 檢查目標變數統計資訊
print(f"\n目標變數統計資訊:")
print(diabetes_df['target'].describe())

# %%
# 資料視覺化 - 使用 seaborn
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# 1. 目標變數分布
sns.histplot(data=diabetes_df, x='target', bins=20, ax=axes[0, 0])
axes[0, 0].set_title('Target Variable Distribution')
axes[0, 0].set_xlabel('Diabetes Progression')
axes[0, 0].set_ylabel('Frequency')

# 2. 特徵與目標變數的相關性
correlation = diabetes_df.corr()['target'].drop('target').sort_values(key=abs, ascending=False)
corr_df = pd.DataFrame({'feature': correlation.index, 'correlation': correlation.values})
sns.barplot(data=corr_df, x='correlation', y='feature', ax=axes[0, 1])
axes[0, 1].set_title('Feature-Target Correlation')
axes[0, 1].set_xlabel('Correlation')

# 3. 重要特徵的散佈圖
important_features = correlation.head(4).index.tolist()
for i, feature in enumerate(important_features):
    row = (i + 2) // 3
    col = (i + 2) % 3
    sns.scatterplot(data=diabetes_df, x=feature, y='target', alpha=0.6, ax=axes[row, col])
    axes[row, col].set_xlabel(feature.title())
    axes[row, col].set_ylabel('Target Value')
    axes[row, col].set_title(f'{feature.title()} vs Target Value')

plt.tight_layout()
plt.savefig('part2_data_visualization.png')
print("\nℹ️  Part 2 資料視覺化圖表已儲存至 'part2_data_visualization.png'")
plt.close() # 關閉圖表以釋放資源

# %%
# 開始 PyCaret 回歸任務
print("\n🚀 開始 PyCaret 回歸工作流程...")

import pycaret.regression as pr

# 1. 設定實驗環境（包含特徵工程）
print("\n1️⃣ 設定實驗環境（包含自動特徵工程）...")
reg_exp = pr.setup(data=diabetes_df, 
               target='target', 
               session_id=123,
               train_size=0.8,
               normalize=True,  # 標準化
               polynomial_features=True)  # 多項式特徵

print("✅ 實驗環境設定完成（含自動特徵工程）")

# 2. 比較多種回歸模型
print("\n2️⃣ 比較多種回歸模型...")
best_models = pr.compare_models(
    include=['lr', 'rf', 'et', 'gbr', 'ridge', 'lasso'],
    sort='R2',
    n_select=3
)

print("✅ 模型比較完成，已選出最佳的3個模型")

# 3. 創建最佳模型
print("\n3️⃣ 創建最佳模型...")
best_model = pr.create_model('rf')  # Random Forest
print("✅ Random Forest 回歸模型創建完成")

# 4. 調整超參數
print("\n4️⃣ 調整超參數...")
tuned_model = pr.tune_model(best_model, optimize='R2')
print("✅ 超參數調整完成")

# 5. 評估模型
print("\n5️⃣ 評估調整後的模型...")
pr.evaluate_model(tuned_model)

# 6. 預測測試集
print("\n6️⃣ 預測測試集...")
predictions = pr.predict_model(tuned_model)
print("✅ 測試集預測完成")
print(f"預測結果形狀: {predictions.shape}")

# 7. 完成最終模型
print("\n7️⃣ 完成最終模型...")
final_model = pr.finalize_model(tuned_model)
print("✅ 最終模型完成")

# 8. 部署準備
print("\n8️⃣ 保存模型...")
pr.save_model(final_model, 'diabetes_regression_model')
print("✅ 模型已保存為 'diabetes_regression_model.pkl'")

# 9. 模型解釋
print("\n9️⃣ 模型解釋 (使用 plot_model)...")
# interpret_model 在某些 PyCaret 版本中對回歸任務支援不佳，我們改用 plot_model 來展示模型解釋性
print("\n特徵重要性 (Feature Importance):")
pr.plot_model(final_model, plot = 'feature')
print("\n殘差圖 (Residuals Plot):")
pr.plot_model(final_model, plot = 'residuals')
print("\n預測誤差圖 (Prediction Error Plot):")
pr.plot_model(final_model, plot = 'error')

# %%
# ============================================================================
# Part 3: PyCaret vs Scikit-learn 比較
# ============================================================================

print("\n\n⚖️ Part 3: PyCaret vs Scikit-learn 比較")
print("-" * 50)

comparison_table = """
特性比較表:
┌─────────────────┬──────────────────┬──────────────────┐
│ 比較項目        │ PyCaret          │ Scikit-learn     │
├─────────────────┼──────────────────┼──────────────────┤
│ 學習曲線        │ 低代碼，易上手   │ 需要更多程式基礎 │
│ 代碼量          │ 極少             │ 相對較多         │
│ 自動化程度      │ 高度自動化       │ 需手動配置       │
│ 特徵工程        │ 自動化           │ 需手動實現       │
│ 模型比較        │ 一鍵比較多種模型 │ 需逐一訓練比較   │
│ 超參數調優      │ 自動化           │ 需手動設計       │
│ 視覺化          │ 內建豐富圖表     │ 需額外程式碼     │
│ 可客製化程度    │ 相對受限         │ 高度客製化       │
│ 執行效率        │ 較慢（封裝層多） │ 較快             │
│ 適用場景        │ 快速原型開發     │ 深度客製化需求   │
└─────────────────┴──────────────────┴──────────────────┘
"""

print(comparison_table)

# %%
# ============================================================================
# Part 4: 自動化機器學習工作流程總結
# ============================================================================

print("\n\n🔄 Part 4: 自動化機器學習工作流程總結")
print("-" * 50)

workflow_steps = """
PyCaret AutoML 工作流程:

1. 📊 資料準備與探索
   └── 載入資料、檢查品質、基本統計

2. 🔧 setup() - 實驗環境設定
   ├── 定義目標變數
   ├── 分割訓練/測試集
   ├── 自動特徵工程
   └── 資料前處理

3. 🏆 compare_models() - 模型比較
   ├── 自動訓練多種演算法
   ├── 交叉驗證評估
   └── 排序選出最佳模型

4. 🎯 create_model() - 創建特定模型
   └── 訓練指定的機器學習演算法

5. ⚙️ tune_model() - 超參數調優
   ├── 自動化超參數搜索
   └── 優化模型性能

6. 📈 evaluate_model() - 模型評估
   ├── 產生評估報告
   ├── 視覺化模型性能
   └── 特徵重要性分析

7. 🔮 predict_model() - 模型預測
   └── 在測試集上進行預測

8. ✅ finalize_model() - 完成模型
   └── 在完整資料集上重新訓練

9. 💾 save_model() - 保存模型
   └── 將模型保存為 pickle 檔案

10. 🚀 deploy_model() - 模型部署
    └── 部署到雲端平台或本地伺服器
"""

print(workflow_steps)

# %%
# ============================================================================
# 學習建議與最佳實踐
# ============================================================================

print("\n\n💡 學習建議與最佳實踐")
print("-" * 50)

best_practices = """
🎯 使用建議:

初學者階段:
• 先從 PyCaret 開始，快速體驗機器學習流程
• 理解各種評估指標的意義
• 學會解讀模型評估結果

進階階段:
• 學習 Scikit-learn，掌握底層原理
• 了解不同演算法的適用場景
• 學習特徵工程技巧

專業應用:
• 根據專案需求選擇合適工具
• PyCaret 適合快速原型開發
• Scikit-learn 適合生產環境部署

⚠️ 注意事項:
• 自動化不代表不需要領域知識
• 始終要理解資料和業務背景
• 模型解釋比性能更重要
• 避免過度依賴自動化工具
"""

print(best_practices)

print("\n🎓 PyCaret AutoML 學習重點總結:")
print("1. PyCaret 大幅簡化了機器學習工作流程")
print("2. 低代碼方式讓初學者更容易入門")
print("3. 自動化特徵工程和超參數調優")
print("4. 內建豐富的視覺化和評估工具")
print("5. 適合快速原型開發和概念驗證")
print("6. 理解工作流程比工具使用更重要")

print("\n✅ PyCaret AutoML 操作練習完成！")
print("📝 建議接下來練習: 使用真實資料集進行完整的 ML 專案") 