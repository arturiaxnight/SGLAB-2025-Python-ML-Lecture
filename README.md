# SGLAB 2025 Python 與機器學習分析課程

## 課程大綱

本課程旨在引導學員入門 Python 程式設計，掌握資料分析與視覺化的核心技能，並初步探索機器學習的基本概念與應用，最終結合 CANTAB 資料進行實戰分析。課程共分為四個階段，每堂課後均有練習作業以鞏固學習成效。

---

## 課前準備：Windows 環境設定 (WSL)
*   **目標：** 為 Windows 使用者建立一個推薦的開發環境。
*   **內容：**
    *   介紹 Windows Subsystem for Linux (WSL) 的概念與優勢。
    *   指導如何啟用 WSL 功能並安裝一個 Linux 發行版 (例如 Ubuntu)。
    *   建議參考 [Microsoft 官方 WSL 安裝指南](https://learn.microsoft.com/zh-tw/windows/wsl/install)。
*   **練習：** 在自己的 Windows 電腦上成功安裝並啟動 WSL 環境。

---

### 第一階段：Python 基礎入門

**Lesson 1: Python 簡介、安裝、環境設定**
*   **內容：**
    *   編譯器 (開發環境) 選擇
    *   透過 Anaconda 進行開發環境管理 (含套件安裝)
*   **練習：** 從零開始，在個人電腦上部署 Python 分析環境。

**Lesson 2: Python 基本語法**
*   **內容：**
    *   變數、資料型態 (int, float, string 等)
    *   判斷式原理 (if/else)
    *   迴圈原理 (for loop)
*   **練習：** 使用迴圈與判斷式撰寫一個簡單的應用，例如計算 BMI 並根據數值判斷體重狀況。

**Lesson 3: Python 常用資料結構**
*   **內容：**
    *   List, Tuple, Dictionary 資料結構介紹與操作
    *   資料的存入、修改、讀取方法
*   **練習：** 透過迴圈生成測試用資料集，以便未來測試函式時進行偵錯。

---

### 第二階段：資料分析與視覺化

**Lesson 4: Pandas 使用**
*   **內容：**
    *   Pandas 分析套件介紹
    *   使用 Pandas 處理 CSV 或 Excel 檔案
    *   合併與編輯多個來源檔案
*   **練習：** 使用 Pandas 內建的 toy dataset 進行資料操作練習，例如刪除特定欄位、建立新的資料集。

**Lesson 5: Matplotlib & Seaborn**
*   **內容：**
    *   介紹 Matplotlib 與 Seaborn 視覺化套件
    *   以實際論文圖表為例，教學繪製 box plot, scatter plot 等圖形，包含細部語法調整
*   **練習：** 尋找幾篇感興趣的論文，練習使用 toy dataset 重現論文中的圖表。

---

### 第三階段：機器學習入門

**Lesson 6: 機器學習基礎概念**
*   **內容：**
    *   機器學習主要分類與概念 (監督式/非監督式學習)
    *   常用術語講解 (Feature, Model, Algorithm)
*   **練習：** 每位學員尋找一篇將機器學習應用於精神科領域的論文，與大家分享該研究使用的 ML 方法類型以及資料處理方式。

**Lesson 7: Scikit-learn & Pycaret AutoML 實際操作練習**
*   **內容：**
    *   介紹 Scikit-learn 機器學習套件
    *   介紹 Pycaret 自動化機器學習套件
    *   實際教學如何應用這兩套工具建立與評估機器學習模型 (回歸/分類)
*   **練習：** 使用 Scikit-learn/Pycaret 內的 toy dataset 進行分類與回歸模型的建立與評估，並結合先前所學的視覺化方法，產生一份完整的分析報告。

**Lesson 8: 模型評估 & 優化**
*   **內容：**
    *   學習超參數 (Hyperparameter) 的概念
    *   如何調整模型以提升效能 (Hyperparameter Tuning)
*   **練習：** 查閱文件，探討上一個練習中的模型是否有可優化的超參數，實際進行調整並比較前後的效能差異。

---

### 第四階段：CANTAB X 機器學習 (量表 CBCL BRIEF……)

**Lesson 9: CANTAB 資料結構**
*   **內容：**
    *   講解 CANTAB 各項測驗的報告結構與特徵 (Feature) 架構
*   **練習：** 詳讀 CANTAB 手冊與相關研究，探討為何過去研究可能只選用部分特徵，思考是否有其他潛在特徵對分析亦有助益。

**Lesson 10: 實際使用 CANTAB 資料進行 ML 分析**
*   **內容：**
    *   根據個人興趣，選擇單一 CANTAB 測驗項目，應用所學知識進行分析
*   **練習：** 整合課程所學的所有內容，分析實驗室收集的實際 CANTAB 資料。

--- 
