# %%
"""
Lesson 7: Scikit-learn 機器學習套件實際操作練習
===================================================

本範例介紹如何使用 Scikit-learn 進行分類與回歸模型的建立與評估
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer, make_classification, make_regression
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC, SVR
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

# Set up matplotlib parameters
plt.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("Lesson 7: Scikit-learn 機器學習套件實際操作練習")
print("=" * 60)

# %%

# ============================================================================
# Part 1: 分類問題 (Classification) - 使用乳腺癌資料集
# ============================================================================

print("\n📊 Part 1: 分類問題 - 乳腺癌資料集")
print("-" * 50)

# 載入乳腺癌資料集
cancer = load_breast_cancer()
X_cancer = cancer.data
y_cancer = cancer.target

# 將資料轉換為 DataFrame 方便操作
cancer_df = pd.DataFrame(X_cancer, columns=cancer.feature_names)
cancer_df['diagnosis'] = y_cancer
cancer_df['diagnosis_name'] = cancer_df['diagnosis'].map({0: 'malignant', 1: 'benign'})

print(f"資料形狀: {cancer_df.shape}")
print(f"特徵數量: {len(cancer.feature_names)}")
print(f"分類標籤: {cancer.target_names}")
print(f"惡性腫瘤樣本數: {(y_cancer == 0).sum()}")
print(f"良性腫瘤樣本數: {(y_cancer == 1).sum()}")
print("\n資料集描述:")
print("威斯康辛乳腺癌資料集包含569個樣本和30個特徵")
print("特徵包括細胞核的半徑、質地、周長、面積、平滑度等")
print("目標是預測腫瘤是惡性(malignant=0)還是良性(benign=1)")
print("\n前5筆資料:")
print(cancer_df.head())

# %%
# 資料視覺化
plt.figure(figsize=(18, 12))

# Select some important features for visualization
important_features = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness']

# 1. Diagnosis distribution
plt.subplot(2, 4, 1)
cancer_df['diagnosis_name'].value_counts().plot(kind='bar')
plt.title('Diagnosis Distribution')
plt.ylabel('Number of Samples')

# 2. Important features boxplot
plt.subplot(2, 4, 2)
sns.boxplot(data=cancer_df.melt(id_vars=['diagnosis_name'], 
                                value_vars=important_features[:3]), 
            x='variable', y='value', hue='diagnosis_name')
plt.title('Important Features Distribution')
plt.xticks(rotation=45)

# 3-5. Important features scatter plots
for i, feature in enumerate(important_features[:3]):
    plt.subplot(2, 4, i+3)
    sns.scatterplot(data=cancer_df, x=feature, y='mean area', 
                    hue='diagnosis_name', s=30, alpha=0.7)
    plt.title(f'{feature} vs Mean Area')

# 6. Correlation heatmap of first 10 features
plt.subplot(2, 4, 6)
correlation = cancer_df[cancer.feature_names[:10]].corr()
sns.heatmap(correlation, annot=False, cmap='coolwarm', center=0)
plt.title('First 10 Features Correlation')

# 7. Feature importance (using simple statistics)
plt.subplot(2, 4, 7)
feature_means = cancer_df.groupby('diagnosis_name')[important_features].mean()
feature_diff = abs(feature_means.loc['malignant'] - feature_means.loc['benign'])
feature_diff.plot(kind='bar')
plt.title('Malignant vs Benign Feature Difference')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# %%
# Split training and testing data
X_train_cancer, X_test_cancer, y_train_cancer, y_test_cancer = train_test_split(
    X_cancer, y_cancer, test_size=0.3, random_state=42, stratify=y_cancer
)

print(f"\n訓練資料形狀: {X_train_cancer.shape}")
print(f"測試資料形狀: {X_test_cancer.shape}")

# Feature standardization
scaler_cancer = StandardScaler()
X_train_cancer_scaled = scaler_cancer.fit_transform(X_train_cancer)
X_test_cancer_scaled = scaler_cancer.transform(X_test_cancer)

# %%
# Build multiple classification models
classifiers = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(kernel='rbf', random_state=42)
}

classification_results = {}

print("\n🤖 訓練分類模型...")
for name, clf in classifiers.items():
    print(f"\n{name}:")
    
    # Train model
    if name == 'SVM':
        clf.fit(X_train_cancer_scaled, y_train_cancer)
        y_pred = clf.predict(X_test_cancer_scaled)
    else:
        clf.fit(X_train_cancer, y_train_cancer)
        y_pred = clf.predict(X_test_cancer)
    
    # Evaluate model
    accuracy = accuracy_score(y_test_cancer, y_pred)
    cv_scores = cross_val_score(clf, X_train_cancer if name != 'SVM' else X_train_cancer_scaled, 
                                y_train_cancer, cv=5)
    
    classification_results[name] = {
        'accuracy': accuracy,
        'cv_mean': cv_scores.mean(),
        'cv_std': cv_scores.std(),
        'predictions': y_pred
    }
    
    print(f"  測試準確率: {accuracy:.4f}")
    print(f"  交叉驗證平均: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# %%
# Visualize classification results
plt.figure(figsize=(15, 5))

for i, (name, results) in enumerate(classification_results.items()):
    plt.subplot(1, 3, i+1)
    cm = confusion_matrix(y_test_cancer, results['predictions'])
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=cancer.target_names,
                yticklabels=cancer.target_names)
    plt.title(f'{name}\nAccuracy: {results["accuracy"]:.4f}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')

plt.tight_layout()
plt.show()

# %%
# ============================================================================
# Part 2: 回歸問題 (Regression) - 使用合成資料集
# ============================================================================

print("\n\n📈 Part 2: 回歸問題 - 合成資料集")
print("-" * 50)

# Create synthetic regression dataset
X_reg, y_reg = make_regression(n_samples=500, n_features=5, noise=0.1, random_state=42)

# Convert to DataFrame
feature_names = [f'feature_{i+1}' for i in range(X_reg.shape[1])]
reg_df = pd.DataFrame(X_reg, columns=feature_names)
reg_df['target'] = y_reg

print(f"回歸資料形狀: {reg_df.shape}")
print("\n前5筆資料:")
print(reg_df.head())

# %%
# Regression data visualization
plt.figure(figsize=(15, 8))

# 1. Feature vs target relationship
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.scatter(reg_df[f'feature_{i+1}'], reg_df['target'], alpha=0.6)
    plt.xlabel(f'Feature {i+1}')
    plt.ylabel('Target Value')
    plt.title(f'Feature {i+1} vs Target Value')

# 6. Correlation heatmap
plt.subplot(2, 3, 6)
correlation = reg_df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Feature Correlation')

plt.tight_layout()
plt.show()

# %%
# Split training and testing data
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.3, random_state=42
)

# Feature standardization
scaler_reg = StandardScaler()
X_train_reg_scaled = scaler_reg.fit_transform(X_train_reg)
X_test_reg_scaled = scaler_reg.transform(X_test_reg)

# Build multiple regression models
regressors = {
    'Linear Regression': LinearRegression(),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'SVM': SVR(kernel='rbf')
}

regression_results = {}

print("\n🤖 訓練回歸模型...")
for name, reg in regressors.items():
    print(f"\n{name}:")
    
    # Train model
    if name == 'SVM':
        reg.fit(X_train_reg_scaled, y_train_reg)
        y_pred = reg.predict(X_test_reg_scaled)
    else:
        reg.fit(X_train_reg, y_train_reg)
        y_pred = reg.predict(X_test_reg)
    
    # Evaluate model
    mse = mean_squared_error(y_test_reg, y_pred)
    mae = mean_absolute_error(y_test_reg, y_pred)
    r2 = r2_score(y_test_reg, y_pred)
    
    regression_results[name] = {
        'mse': mse,
        'mae': mae,
        'r2': r2,
        'predictions': y_pred
    }
    
    print(f"  均方誤差 (MSE): {mse:.4f}")
    print(f"  平均絕對誤差 (MAE): {mae:.4f}")
    print(f"  R² 分數: {r2:.4f}")

# %%
# Visualize regression results
plt.figure(figsize=(15, 5))

for i, (name, results) in enumerate(regression_results.items()):
    plt.subplot(1, 3, i+1)
    plt.scatter(y_test_reg, results['predictions'], alpha=0.6)
    plt.plot([y_test_reg.min(), y_test_reg.max()], 
             [y_test_reg.min(), y_test_reg.max()], 'r--', lw=2)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title(f'{name}\nR² = {results["r2"]:.4f}')

plt.tight_layout()
plt.show()

# %%
# ============================================================================
# Part 3: 超參數調優示例
# ============================================================================

print("\n\n⚙️ Part 3: 超參數調優示例")
print("-" * 50)

# Use Random Forest for hyperparameter tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10]
}

rf_classifier = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(rf_classifier, param_grid, cv=5, scoring='accuracy', n_jobs=-1)

print("🔍 進行網格搜索...")
grid_search.fit(X_train_cancer, y_train_cancer)

print(f"最佳參數: {grid_search.best_params_}")
print(f"最佳交叉驗證分數: {grid_search.best_score_:.4f}")

# Evaluate model with best parameters
best_rf = grid_search.best_estimator_
y_pred_best = best_rf.predict(X_test_cancer)
best_accuracy = accuracy_score(y_test_cancer, y_pred_best)

print(f"優化後測試準確率: {best_accuracy:.4f}")

# %%
# ============================================================================
# Summary Report
# ============================================================================

print("\n\n📋 模型效能總結報告")
print("=" * 60)

print("\n分類模型結果:")
print("-" * 30)
for name, results in classification_results.items():
    print(f"{name:20s} - 準確率: {results['accuracy']:.4f}")

print("\n回歸模型結果:")
print("-" * 30)
for name, results in regression_results.items():
    print(f"{name:20s} - R²: {results['r2']:.4f}, MSE: {results['mse']:.4f}")

print(f"\n超參數優化結果:")
print("-" * 30)
print(f"Random Forest 原始準確率: {classification_results['Random Forest']['accuracy']:.4f}")
print(f"Random Forest 優化後準確率: {best_accuracy:.4f}")
print(f"改善程度: {((best_accuracy - classification_results['Random Forest']['accuracy']) * 100):.2f}%")

print("\n🎓 學習重點總結:")
print("1. Scikit-learn 提供了完整的機器學習工具組")
print("2. 乳腺癌資料集是經典的二元分類問題 (惡性/良性)")
print("3. 高維資料集 (30個特徵) 需要適當的特徵選擇和視覺化")
print("4. 特徵標準化對某些演算法很重要")
print("5. 交叉驗證可以更好地評估模型泛化能力")
print("6. 超參數調優可以進一步提升模型效能")
print("7. 視覺化是理解模型結果的重要工具")

print("\n✅ Scikit-learn 基礎操作練習完成！") 