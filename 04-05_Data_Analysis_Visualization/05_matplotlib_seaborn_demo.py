# pip install seaborn scikit-learn
#%% 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

#%% 設定 Seaborn 樣式，使圖表更美觀
sns.set_theme(style="whitegrid")

#%% 1. 載入與準備資料
# 載入鳶尾花資料集
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# 轉換為 Pandas DataFrame
df_iris = pd.DataFrame(X, columns=feature_names)
df_iris['species'] = pd.Categorical.from_codes(y, target_names)

print("First five records of the Iris dataset:")
print(df_iris.head())
print("\nDataset basic information:")
df_iris.info()
print("\nNumber of Iris flowers in each class:")
print(df_iris['species'].value_counts())

#%% 2. 使用 Matplotlib 繪圖

# 選擇兩個特徵進行繪圖，例如：花萼長度 (sepal length) 與 花萼寬度 (sepal width)
x_feature_idx = 0  # sepal length (cm)
y_feature_idx = 1  # sepal width (cm)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(X[:, x_feature_idx], X[:, y_feature_idx], c=y, cmap='viridis', edgecolor='k')
plt.xlabel(feature_names[x_feature_idx])
plt.ylabel(feature_names[y_feature_idx])
plt.title('Matplotlib: Iris Species Scatter Plot (Sepal Length vs Sepal Width)')
# 加上圖例
handles, _ = scatter.legend_elements()
plt.legend(handles, target_names, title="Species")
plt.show()

# 繪製盒鬚圖，比較不同種類鳶尾花在各特徵上的分佈
plt.figure(figsize=(12, 8))
for i in range(X.shape[1]):
    plt.subplot(2, 2, i + 1)
    # 建立一個列表，包含每個種類在該特徵上的數據
    data_to_plot = [X[y == j, i] for j in range(len(target_names))]
    plt.boxplot(data_to_plot, labels=target_names)
    plt.title(f'Matplotlib: {feature_names[i]} Distribution')
    plt.ylabel(feature_names[i])
    plt.xlabel("Species")
plt.tight_layout() # 自動調整子圖參數，使其適應視窗大小
plt.show()

#%% 3. 使用 Seaborn 繪圖

# 使用 Seaborn 繪製散佈圖
plt.figure(figsize=(10, 6))
sns.scatterplot(x=feature_names[x_feature_idx], y=feature_names[y_feature_idx], hue='species', data=df_iris, palette='viridis', s=100, edgecolor='k')
plt.title('Seaborn: Iris Species Scatter Plot (Sepal Length vs Sepal Width)')
plt.show()

# 使用 Seaborn 繪製盒鬚圖
plt.figure(figsize=(12, 8))
for i, feature in enumerate(feature_names):
    plt.subplot(2, 2, i + 1)
    sns.boxplot(x='species', y=feature, data=df_iris, palette='pastel')
    plt.title(f'Seaborn: {feature} Distribution')
plt.tight_layout()
plt.show()

# 使用 Seaborn pairplot 觀察所有特徵間的關係
# pairplot 會顯示每對特徵之間的散佈圖，以及每個特徵的直方圖或密度圖 (對角線)
print("\nPlotting Seaborn Pairplot, this may take some time...")
sns.pairplot(df_iris, hue='species', palette='viridis', diag_kind='kde') # diag_kind 可以是 'hist' 或 'kde'
plt.suptitle('Seaborn Pairplot: Iris Feature Relationships', y=1.02) # y=1.02 調整主標題位置
plt.show()

#%% 4. 結合 SVM 與視覺化
# 為了視覺化決策邊界，我們通常選擇兩個特徵
# 這裡我們選擇花瓣長度 (petal length) 和花瓣寬度 (petal width)，因為它們通常能提供較好的分類效果
X_svm = iris.data[:, 2:4] # 使用花瓣長度 (petal length) 和花瓣寬度 (petal width)
y_svm = iris.target

# 資料標準化
scaler = StandardScaler()
X_svm_scaled = scaler.fit_transform(X_svm)

# 分割訓練集和測試集 (雖然這裡主要用於視覺化，但仍是好習慣)
X_train, X_test, y_train, y_test = train_test_split(X_svm_scaled, y_svm, test_size=0.3, random_state=42, stratify=y_svm)

# 訓練 SVM 模型
svm_model = SVC(kernel='linear', C=1.0, random_state=42) # 線性核函數
# svm_model = SVC(kernel='rbf', C=1.0, gamma='auto', random_state=42) # RBF 核函數 (更彈性)
svm_model.fit(X_train, y_train)

print(f"\nSVM model accuracy on the test set: {svm_model.score(X_test, y_test):.2f}")

# 繪製決策邊界
plt.figure(figsize=(10, 7))

# 創建網格來繪製決策邊界
x_min, x_max = X_svm_scaled[:, 0].min() - 0.5, X_svm_scaled[:, 0].max() + 0.5
y_min, y_max = X_svm_scaled[:, 1].min() - 0.5, X_svm_scaled[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# 預測網格中每個點的類別
Z = svm_model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 繪製等高線圖 (決策邊界)
plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')

# 繪製訓練數據點
scatter_svm = plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='viridis', edgecolor='k', s=50, label='Training Data')
# 繪製測試數據點 (可選，用於觀察模型在未見數據上的表現)
# plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='viridis', marker='x', s=100, label='測試資料')


plt.xlabel(f"Standardized {feature_names[2]}")
plt.ylabel(f"Standardized {feature_names[3]}")
plt.title('SVM Decision Boundary (Petal Length vs Petal Width)')

# 加上圖例 (處理 matplotlib 顏色對應問題)
handles, _ = scatter_svm.legend_elements(prop="colors") # 使用 prop="colors" 來取得正確的圖例顏色
legend_labels = [f"{target_names[int(label.split('{')[-1].split('}')[0])]}" for label in _] # 從內部標籤提取類別名稱

# 如果使用RBF核，可以加上支持向量的視覺化
if svm_model.kernel == 'rbf' or svm_model.kernel == 'linear': # 線性核也有支持向量
    sv = svm_model.support_vectors_
    plt.scatter(sv[:, 0], sv[:, 1], s=100, facecolors='none', edgecolors='red', label='Support Vectors')

plt.legend(handles, target_names, title="Species")
plt.show()

#%% 總結與參考資料
print("\nEnd of Lesson 5 Matplotlib and Seaborn examples.")
print("You can try modifying feature selection, SVM model parameters (e.g., kernel, C value), or use other toy datasets for practice.")
print(f"Reference: Scikit-learn Toy Datasets - {iris.DESCR.split('---')[0].strip()}") # 簡短引用
print("Scikit-learn Toy Datasets webpage: https://scikit-learn.org/stable/datasets/toy_dataset.html")
