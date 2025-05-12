# Anaconda 安裝與環境設定教學

本教學將引導您如何在您的作業系統 (Windows, macOS, Linux) 上安裝 Anaconda Distribution，並建立一個獨立的 Python 開發環境。

## 什麼是 Anaconda？

Anaconda 是一個廣受歡迎的 Python 和 R 語言發行版，專為科學計算 (資料科學、機器學習等) 設計。它包含了 `conda` 這個強大的套件管理與環境管理系統，以及超過 300 個常用的資料科學相關套件 (如 NumPy, Pandas, Matplotlib, Scikit-learn 等)。使用 Anaconda 可以大幅簡化環境設定與套件安裝的流程。

參考資料：[Anaconda Documentation](https://www.anaconda.com/docs/main)

## 安裝步驟

1.  **下載 Anaconda Installer:**
    *   前往 Anaconda 官方下載頁面：[https://www.anaconda.com/download/success](https://www.anaconda.com/download/success)
    *   根據您的作業系統 (Windows, macOS, Linux) 選擇對應的 **Graphical Installer (圖形介面安裝程式)**。建議下載最新 Python 版本的安裝程式 (例如 Python 3.12)。
    *   **注意：**
        *   macOS 使用者請根據您的晶片類型 (Apple Silicon 或 Intel) 選擇正確的版本。
        *   檔案較大，下載需要一些時間。

2.  **執行安裝程式:**
    *   下載完成後，執行安裝程式。
    *   **Windows:** 雙擊 `.exe` 檔案。
    *   **macOS:** 雙擊 `.pkg` 檔案。
    *   **Linux:** 開啟終端機，`cd` 到下載目錄，執行 `bash Anaconda3-<version>-Linux-x86_64.sh` (請將 `<version>` 替換為您下載的實際版本號)。
    *   依照安裝程式的指示進行安裝。建議接受預設設定，特別是：
        *   **安裝路徑:** 建議使用預設路徑。
        *   **加入環境變數 (Windows):** **建議勾選** "Add Anaconda3 to my PATH environment variable" (雖然安裝程式可能不建議，但對於初學者在命令提示字元直接使用 `conda` 指令會比較方便)。若不勾選，則需透過 Anaconda Prompt 來操作。
        *   **將 Anaconda 設為預設 Python (Windows/macOS):** 建議勾選 "Register Anaconda3 as my default Python"。

3.  **驗證安裝:**
    *   **Windows:** 開啟 **Anaconda Prompt** (可從「開始」功能表搜尋)。
    *   **macOS/Linux:** 開啟系統的**終端機 (Terminal)**。
    *   在開啟的命令列視窗中輸入以下指令，檢查 `conda` 是否成功安裝：
        ```bash
        conda --version
        ```
        如果看到類似 `conda 23.7.4` 的版本號輸出，代表安裝成功。

## 建立與管理開發環境

使用 `conda` 建立獨立的開發環境是個好習慣，可以避免不同專案之間的套件版本衝突。

1.  **開啟 Anaconda Prompt 或終端機。**

2.  **建立新的環境:**
    使用 `conda create` 指令來建立一個新的環境。我們建立一個名為 `ntuh-ml` 的環境，並指定使用 Python 3.11 版本 (您可以根據需求更改版本)。
    ```bash
    conda create --name ntuh-ml python=3.11
    ```
    *   `--name` 或 `-n` 後面接環境名稱。
    *   `python=3.11` 指定環境中要安裝的 Python 版本。
    *   過程中會提示您是否要安裝一些基礎套件，輸入 `y` 並按下 Enter。

3.  **啟用 (Activate) 環境:**
    建立好環境後，需要啟用它才能在該環境中工作。
    ```bash
    conda activate ntuh-ml
    ```
    *   啟用成功後，命令列提示字元的前面會出現環境名稱，例如 `(ntuh-ml) C:\Users\YourName>`。

4.  **安裝所需套件:**
    在已啟用的環境中，使用 `conda install` 指令安裝課程所需的套件。
    ```bash
    conda install pandas matplotlib seaborn scikit-learn pycaret jupyterlab
    ```
    *   您可以一次安裝多個套件，用空格隔開。
    *   `jupyterlab` 是一個常用的互動式開發環境。
    *   過程中可能會提示您安裝相關依賴套件，輸入 `y` 並按下 Enter。

5.  **查看已安裝的套件:**
    ```bash
    conda list
    ```
    這個指令會列出目前環境中所有已安裝的套件及其版本。

6.  **離開 (Deactivate) 環境:**
    當您想切換回基礎環境或其他環境時，使用以下指令：
    ```bash
    conda deactivate
    ```
    *   命令列提示字元前面的環境名稱會消失。

7.  **查看所有環境:**
    ```bash
    conda env list
    ```
    這個指令會列出您電腦上所有已建立的 conda 環境，目前所在的環境會以星號 `*` 標示。

8.  **刪除環境 (若不再需要):**
    ```bash
    conda remove --name ntuh-ml --all
    ```
    *   請謹慎使用此指令。

## 好用package
pip install jupyter

---

您現在已經成功安裝了 Anaconda 並學會如何建立和管理開發環境。在後續課程中，請記得先 `conda activate ntuh-ml` 進入我們為課程建立的環境再進行操作。 