# WSL 安裝教學 (Windows Subsystem for Linux)

本教學將引導您如何在 Windows 系統上安裝適用於 Linux 的 Windows 子系統 (WSL) 以及 Ubuntu 發行版。WSL 讓您可以在 Windows 環境中直接執行 Linux 應用程式與指令。

## 必要條件

*   您的作業系統必須是 **Windows 10 版本 2004 或更新版本 (組建 19041 或更新版本)** 或 **Windows 11**。

## 安裝步驟

根據 [Microsoft 官方 WSL 安裝指南](https://learn.microsoft.com/zh-tw/windows/wsl/install)，最簡單的安裝方式如下：

1.  **以系統管理員身分開啟 PowerShell 或 Windows 命令提示字元：**
    *   在 Windows 搜尋列輸入 "PowerShell" 或 "cmd"。
    *   在搜尋結果上按滑鼠右鍵。
    *   選擇「以系統管理員身分執行」。

2.  **執行安裝指令：**
    在開啟的系統管理員視窗中，輸入以下指令並按下 Enter：
    ```powershell
    wsl --install
    ```
    *   這個指令會自動啟用 WSL 所需的 Windows 功能，並下載、安裝預設的 Linux 發行版，也就是 **Ubuntu**。

3.  **重新啟動電腦：**
    指令執行完畢後，請依照提示重新啟動您的電腦以完成安裝。

## 首次啟動與設定

1.  **啟動 Ubuntu：** 重新開機後，您可以從「開始」功能表找到並啟動 "Ubuntu"。
2.  **等待安裝完成：** 第一次啟動時，系統會需要一些時間來解壓縮並設定檔案。請稍待片刻。
3.  **建立 Linux 使用者帳戶：** 系統會提示您為 Ubuntu 設定一個新的使用者名稱和密碼。請依照指示完成設定。這個帳號密碼與您的 Windows 帳號密碼是獨立的。

完成以上步驟後，您就成功在 Windows 上安裝了 WSL 與 Ubuntu 環境！您可以開始在 Ubuntu 終端機中使用 Linux 指令了。

## 其他說明

*   如果您想安裝 Ubuntu 以外的 Linux 發行版，可以在 `wsl --install` 指令後加上 `-d` 參數指定，例如：`wsl --install -d Debian`。
*   您可以透過指令 `wsl --list --online` 查看所有可安裝的 Linux 發行版。
*   詳細的資訊與疑難排解，請參閱 [Microsoft 官方 WSL 安裝指南](https://learn.microsoft.com/zh-tw/windows/wsl/install)。 