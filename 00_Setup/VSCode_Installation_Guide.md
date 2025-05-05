# Visual Studio Code (VSCode) 安裝與基本使用教學

本教學將引導您安裝 Visual Studio Code (簡稱 VSCode)，一個強大且免費的程式碼編輯器，並介紹其基本使用方式，特別是針對 Python 開發。

## 什麼是 VSCode？

VSCode 是一個由 Microsoft 開發的輕量級但功能豐富的原始碼編輯器，支援 Windows, macOS 和 Linux。它內建了對 JavaScript, TypeScript 和 Node.js 的支援，並可以透過安裝擴充套件 (Extensions) 來支援幾乎所有程式語言，包含 Python。

VSCode 提供了許多現代化的開發功能，例如語法突顯、智慧程式碼完成 (IntelliSense)、偵錯、內建 Git 版本控制、整合式終端機等。

官方網站：[https://code.visualstudio.com/](https://code.visualstudio.com/)

## 安裝步驟

1.  **下載 VSCode:**
    *   前往 VSCode 官方網站：[https://code.visualstudio.com/](https://code.visualstudio.com/)
    *   網站通常會自動偵測您的作業系統，並提供對應的下載按鈕 (例如 "Download for Windows", "Download for macOS")。
    *   點擊下載按鈕，下載穩定版 (Stable Build) 的安裝程式。
    *   如果需要其他版本 (例如 Linux 的 `.deb` 或 `.rpm` 格式)，可以在下載按鈕下方找到其他平台的連結。

2.  **執行安裝程式:**
    *   下載完成後，執行安裝程式。
    *   **Windows:** 雙擊 `.exe` 檔案。
    *   **macOS:** 將 `Visual Studio Code.app` 拖曳到 "Applications" 資料夾。
    *   **Linux:**
        *   `.deb` (Debian/Ubuntu): `sudo apt install ./<file>.deb`
        *   `.rpm` (Fedora/CentOS): `sudo yum install ./<file>.rpm` 或 `sudo dnf install ./<file>.rpm`
    *   依照安裝程式的指示完成安裝。建議勾選 "將 VS Code 加入 PATH 環境變數" (Add to PATH) 的選項，這樣可以從命令列直接啟動 VSCode。

3.  **啟動 VSCode:**
    *   安裝完成後，您可以從應用程式選單或透過在終端機/命令提示字元輸入 `code` 來啟動 VSCode。

## 基本使用與 Python 設定 (WSL 環境)

由於我們將使用 WSL (Windows Subsystem for Linux) 作為主要的開發環境，VSCode 的設定會稍有不同。我們需要利用 **Remote Development** 擴充套件來連接到 WSL。

1.  **安裝 Remote Development 擴充套件包:**
    *   啟動 VSCode。
    *   點擊左側活動列 (Activity Bar) 上的擴充套件圖示。
    *   在搜尋框中輸入 "Remote Development"。
    *   找到由 Microsoft 發布的 **Remote Development** 擴充套件包 (它會包含 Remote - WSL, Remote - Containers, Remote - SSH 等)，點擊 "Install" 安裝。
    *   安裝這個擴充套件包會自動安裝 **Remote - WSL** 擴充套件。

2.  **連接到 WSL:**
    *   安裝完成後，左下角會出現一個綠色的遠端連接狀態圖示 (通常是 `><`)。
    *   點擊該圖示，或者按下 `Ctrl+Shift+P` (Windows/Linux) 或 `Cmd+Shift+P` (macOS) 開啟命令選擇區，輸入 "WSL: Connect to WSL" 並選擇該命令。
    *   VSCode 會開啟一個新的視窗，這個視窗現在是直接連接到您的 WSL 環境 (例如 Ubuntu)。您可能會需要等待 VSCode 在 WSL 中安裝一些必要的伺服器元件。
    *   連接成功後，左下角的狀態圖示會顯示 "WSL: Ubuntu" (或您安裝的其他發行版名稱)。

3.  **在 WSL 中開啟專案資料夾:**
    *   **重要：** 現在您需要在 WSL 環境中操作檔案系統。
    *   在已連接到 WSL 的 VSCode 視窗中，選擇 "File" > "Open Folder..."。
    *   瀏覽並選擇您在 **WSL 檔案系統內** 的專案資料夾 (例如 `/home/your_wsl_username/projects/ntuh-ml-course`)。
    *   **注意：** 不要選擇 Windows 的路徑 (如 `C:\...`)，除非您有特殊需求。為了獲得最佳效能和相容性，專案檔案應存放在 WSL 檔案系統內。

4.  **在 WSL 環境中安裝 Python 擴充套件:**
    *   **重要：** 擴充套件需要在連接的環境中單獨安裝。
    *   在已連接到 WSL 的 VSCode 視窗中，再次點擊擴充套件圖示。
    *   您會看到擴充套件列表分為 "LOCAL - INSTALLED" 和 "WSL: UBUNTU - INSTALLED" (或類似名稱)。
    *   搜尋 "Python" 擴充套件 (由 Microsoft 發布)，並點擊 "Install in WSL: Ubuntu"。
    *   同樣地，如果您需要 Jupyter 擴充套件，也需要在 WSL 環境中安裝它。

5.  **在 WSL 環境中選擇 Python 解譯器:**
    *   在 WSL 環境中，按下 `Ctrl+Shift+P` 或 `Cmd+Shift+P`。
    *   輸入 "Python: Select Interpreter"。
    *   VSCode 會偵測**WSL 內部**的 Python 環境，包括您在 WSL 中透過 Anaconda 建立的 `ntuh-ml` 環境。
    *   選擇 `ntuh-ml` 環境。
    *   狀態列會顯示從 WSL 環境選中的 Python 解譯器。

6.  **使用整合式終端機 (在 WSL 中):**
    *   在已連接到 WSL 的 VSCode 視窗中開啟整合式終端機 (``Ctrl+` ``)。
    *   這個終端機**就是 WSL 的 Bash 終端機**，並且會自動啟用您選擇的 Python 環境 (例如 `(ntuh-ml)` 提示字元)。
    *   您可以在這裡執行 Linux 指令、Python 腳本 (`python your_script.py`)、使用 `conda` 管理環境和套件 (`conda install ...`)。

7.  **執行 Python 程式碼 (在 WSL 中):**
    *   流程與之前相同，但所有操作都是在 WSL 環境中進行。
    *   建立 `.py` 檔案，編寫程式碼。
    *   使用整合式終端機執行，或點擊右上角的執行按鈕。
