# 第五課作業：乳癌資料集視覺化分析

**目標：** 運用 Matplotlib 與 Seaborn 套件，對 `scikit-learn` 中的 `breast_cancer` (乳癌) 資料集進行探索性資料分析與視覺化。

**資料集：** `sklearn.datasets.load_breast_cancer()`

這個資料集包含從乳腺腫塊的細針穿刺 (FNA) 數位化影像中計算出的特徵。這些特徵描述了影像中細胞核的特性，用於預測腫瘤是惡性還是良性。

**作業要求：**

請建立一個 Python 腳本 (`.py` 檔案) 或 Jupyter Notebook (`.ipynb` 檔案) 來完成以下任務。記得為您的圖表加上適當的標題、座標軸標籤和圖例。

---

### 任務 1：載入與初步探索資料

1.  從 `sklearn.datasets` 載入 `breast_cancer` 資料集。
2.  將特徵資料 (X) 和目標變數 (y) 轉換為 Pandas DataFrame。將特徵名稱賦予欄位，並新增一個名為 `diagnosis` 的欄位來儲存類別資訊 (使用 `target_names` 來表示實際的類別名稱，如 'malignant' 和 'benign')。
3.  印出 DataFrame 的前五筆記錄 (`head()`)。
4.  印出 DataFrame 的基本資訊 (`info()`)。
5.  印出資料集的描述 (`DESCR` 屬性的一部分，例如開頭的摘要)。
6.  計算並印出每個診斷類別 (惡性/良性) 的樣本數量。

---

### 任務 2：使用 Matplotlib 進行視覺化

1.  **散佈圖 (Scatter Plot):**
    *   選擇兩個您認為可能用來區分類別的特徵 (例如 `mean radius` 和 `mean texture`)。
    *   繪製一個散佈圖，其中 X 軸和 Y 軸分別代表您選擇的兩個特徵，點的顏色根據 `diagnosis` 區分。
    *   加上圖例來標示不同類別。
2.  **盒鬚圖 (Box Plot):**
    *   選擇三個特徵 (例如 `mean perimeter`, `mean area`, `mean smoothness`)。
    *   為每個選定的特徵繪製盒鬚圖，比較惡性與良性腫瘤在這三個特徵上的分佈。您可以在一張圖中使用子圖 (subplots) 或分別繪製。

---

### 任務 3：使用 Seaborn 進行視覺化

1.  **散佈圖 (Scatter Plot):**
    *   使用 Seaborn 重新繪製任務 2.1 中的散佈圖 (例如 `mean radius` vs `mean texture`)，利用 `hue` 參數來區分顏色。
2.  **小提琴圖 (Violin Plot):**
    *   選擇一個特徵 (例如 `mean compactness`)。
    *   繪製一個小提琴圖，展示該特徵在不同診斷類別中的分佈情況。小提琴圖結合了盒鬚圖與核心密度估計。
3.  **熱力圖 (Heatmap):**
    *   計算資料集中所有數值特徵的相關係數矩陣。
    *   使用 Seaborn 的 `heatmap` 繪製這個相關係數矩陣的熱力圖，並顯示相關係數的值在格子上。

---

### 任務 4 (進階挑戰)：視覺化模型預測結果

1.  **資料準備與模型訓練：**
    *   選擇兩個您認為在散佈圖上區分效果較好的特徵 (例如 `worst radius` 和 `worst concave points`)。
    *   對選取的特徵資料進行標準化 (`StandardScaler`)。
    *   將資料分割為訓練集與測試集。
    *   使用 `sklearn.linear_model.LogisticRegression` 訓練一個邏輯迴歸模型。
2.  **預測與混淆矩陣視覺化：**
    *   使用訓練好的模型對測試集進行預測。
    *   計算準確率 (accuracy) 和混淆矩陣。
    *   使用 Seaborn 的 `heatmap` 將混淆矩陣視覺化，並在標題中註明準確率。
3.  **(可選) 預測結果散佈圖：**
    *   繪製測試集資料的散佈圖 (使用您在任務 4.1 中選擇的兩個特徵)。
    *   點的顏色根據 **真實類別** 標示。
    *   使用不同的標記 (marker) 來區分模型 **預測正確** 與 **預測錯誤** 的樣本點，並加上清晰的圖例。

---

**提示：**

*   乳癌資料集有 30 個特徵，多嘗試不同的特徵組合來進行視覺化。
*   查閱 Matplotlib 和 Seaborn 的官方文件，探索更多圖表類型和自訂選項。
*   在選擇特徵進行模型訓練時，可以參考您在任務 2 和 3 中所做的視覺化分析，選擇那些看起來能較好區分不同類別的特徵。

祝您練習愉快！ 