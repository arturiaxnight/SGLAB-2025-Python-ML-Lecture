# Lesson 7: Scikit-learn & PyCaret AutoML 實際操作練習

## 📋 課程概述

本課程介紹兩個重要的機器學習套件：
- **Scikit-learn**：Python 最受歡迎的機器學習庫
- **PyCaret**：低代碼自動化機器學習套件

通過實際操作，學員將掌握分類與回歸模型的建立、評估和優化。

### 🎯 交互式學習體驗
本課程採用 `#%%` 代碼塊分割的交互式 Python 文件，支援：
- **VSCode**：原生支援，點擊 "Run Cell" 執行
- **PyCharm**：使用 Ctrl+Enter 執行代碼塊  
- **Spyder**：支援代碼塊執行
- **一般 Python 環境**：可直接執行完整檔案

## 📂 檔案結構

```
06-08_Machine_Learning/
├── README.md                          # 本說明檔案
├── requirements.txt                   # 必要套件清單
├── lesson7_scikit_learn_demo.py      # Scikit-learn 完整示例
├── lesson7_pycaret_demo.py           # PyCaret AutoML 示例
└── lesson7_interactive_demo.py       # 交互式教學（推薦使用）
```

## 🚀 快速開始

### 1. 環境準備

```bash
# 安裝必要套件
pip install -r requirements.txt

# 或使用 conda
conda install --file requirements.txt
```

### 2. 運行範例

#### 方式一：交互式執行（推薦）
```bash
# 使用 VSCode 開啟交互式檔案
code lesson7_interactive_demo.py

# 在 VSCode 中點擊 "Run Cell" 或使用 Ctrl+Enter 執行每個 #%% 代碼塊
# 在 PyCharm 中使用 Ctrl+Enter 執行代碼塊
```

#### 方式二：直接執行完整 Python 檔案
```bash
# 執行 Scikit-learn 示例
python lesson7_scikit_learn_demo.py

# 執行 PyCaret 示例
python lesson7_pycaret_demo.py

# 執行交互式示例
python lesson7_interactive_demo.py
```

## 📊 學習內容

### Part 1: Scikit-learn 基礎操作

#### 1.1 分類問題
- **資料集**：鳶尾花（Iris）資料集
- **演算法**：邏輯回歸、隨機森林、支援向量機
- **評估指標**：準確率、交叉驗證、混淆矩陣

#### 1.2 回歸問題
- **資料集**：糖尿病進展資料集
- **演算法**：線性回歸、隨機森林回歸、支援向量迴歸
- **評估指標**：均方誤差（MSE）、平均絕對誤差（MAE）、R² 分數

#### 1.3 超參數調優
- 使用 GridSearchCV 進行網格搜索
- 比較優化前後的模型效能
- 理解超參數對模型性能的影響

### Part 2: PyCaret AutoML 體驗

#### 2.1 自動化分類
- 一鍵環境設定（setup）
- 多模型比較（compare_models）
- 自動超參數調優（tune_model）
- 模型評估與視覺化（evaluate_model）

#### 2.2 自動化回歸
- 自動特徵工程（多項式特徵、特徵交互作用）
- 標準化與正規化
- 模型解釋（interpret_model）
- 模型部署準備

### Part 3: 工具比較與最佳實踐

| 比較項目 | PyCaret | Scikit-learn |
|----------|---------|--------------|
| 學習曲線 | 低代碼，易上手 | 需要更多程式基礎 |
| 代碼量 | 極少 | 相對較多 |
| 自動化程度 | 高度自動化 | 需手動配置 |
| 特徵工程 | 自動化 | 需手動實現 |
| 可客製化程度 | 相對受限 | 高度客製化 |
| 適用場景 | 快速原型開發 | 深度客製化需求 |

## 🎯 學習目標

完成本課程後，學員將能夠：

1. **理解機器學習工作流程**
   - 資料探索與前處理
   - 模型訓練與驗證
   - 性能評估與優化

2. **使用 Scikit-learn**
   - 建立分類與回歸模型
   - 進行交叉驗證
   - 實施超參數調優
   - 視覺化模型結果

3. **使用 PyCaret**
   - 快速設定 ML 實驗
   - 比較多種演算法
   - 自動化特徵工程
   - 產生模型評估報告

4. **選擇合適工具**
   - 根據專案需求選擇工具
   - 理解各工具的優缺點
   - 制定 ML 專案策略

## 📝 課後練習

### 練習 1：基礎實作（必做）
使用 Scikit-learn 內建的其他資料集（如波士頓房價、手寫數字）：
1. 完成完整的 ML 工作流程
2. 比較至少 3 種不同演算法
3. 進行超參數調優
4. 製作視覺化報告

### 練習 2：PyCaret 進階（選做）
如果已安裝 PyCaret：
1. 探索所有可用的模型比較
2. 使用自動特徵工程功能
3. 嘗試模型融合（ensemble）
4. 練習模型解釋技巧

### 練習 3：整合應用（挑戰）
結合前面課程學到的技能：
1. 使用 Pandas 處理真實資料
2. 運用 Matplotlib/Seaborn 製作專業圖表
3. 撰寫完整的分析報告
4. 為下一階段的 CANTAB 資料分析做準備

## 🔍 常見問題

### Q1: PyCaret 安裝失敗怎麼辦？
**A**: PyCaret 依賴較多，建議：
```bash
# 先更新 pip
pip install --upgrade pip

# 在虛擬環境中安裝
conda create -n pycaret_env python=3.8
conda activate pycaret_env
pip install pycaret
```

### Q2: 如何選擇分類還是回歸？
**A**: 根據目標變數類型：
- **分類**：目標是離散類別（如疾病診斷、垃圾郵件分類）
- **回歸**：目標是連續數值（如房價預測、股價預測）

### Q3: 模型準確率不高怎麼辦？
**A**: 可以嘗試：
1. 增加更多特徵或改善特徵工程
2. 嘗試不同的演算法
3. 調整超參數
4. 檢查資料品質和平衡性
5. 收集更多訓練資料

### Q4: 何時使用 PyCaret，何時使用 Scikit-learn？
**A**: 
- **PyCaret**：快速原型開發、探索性分析、初學者學習
- **Scikit-learn**：生產環境、需要細緻控制、客製化需求

## 📚 延伸學習資源

### 官方文檔
- [Scikit-learn 官方文檔](https://scikit-learn.org/stable/)
- [PyCaret 官方文檔](https://pycaret.gitbook.io/docs/)

### 推薦教程
- [Scikit-learn 用戶指南](https://scikit-learn.org/stable/user_guide.html)
- [PyCaret 教程合集](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog)

### 實踐專案
- [Kaggle 機器學習競賽](https://www.kaggle.com/competitions)
- [UCI 機器學習資料庫](https://archive.ics.uci.edu/ml/index.php)

## 🎯 下一步學習計劃

完成本課程後，建議學習順序：

1. **Lesson 8**: 模型評估 & 優化
   - 深度學習交叉驗證策略
   - 學習曲線分析
   - 模型選擇技巧

2. **進階主題**：
   - 集成學習（Ensemble Learning）
   - 特徵選擇與降維
   - 不平衡資料處理

3. **實際應用**：
   - CANTAB 資料分析
   - 醫療資料機器學習
   - 模型部署與監控

---

## 📞 技術支援

如遇到問題，請：
1. 檢查 requirements.txt 中的套件版本
2. 查看錯誤訊息並搜尋解決方案
3. 參考官方文檔
4. 在課程群組中提問

**祝學習愉快！🎉** 