# GitHub Copilot 申請與設定教學

本教學將引導您如何申請 GitHub Copilot，這是一個強大的 AI 程式碼輔助工具，並說明如何將其整合到 VS Code 中。

## 什麼是 GitHub Copilot？

GitHub Copilot 是一個由 GitHub 和 OpenAI 開發的 AI 程式碼助手，可以在您編寫程式碼時提供即時的建議和自動完成。它可以幫助您更快地編寫程式碼、學習新的程式語言和框架，並減少重複性的工作。它可以理解程式碼的上下文，並根據您的註解或現有程式碼生成相關的程式碼片段，甚至整個函式。

參考資料：[GitHub Copilot 官網](https://github.com/features/copilot)

## 資格與方案

GitHub Copilot 提供不同的方案：

*   **Free (免費方案):**
    *   提供有限的每月請求次數 (50 次 agent mode/chat，2000 次 completions)。
    *   可使用 Claude 3.5 Sonnet, GPT-4o 等模型。
    *   適合剛開始試用的個人開發者。
*   **Pro (專業版):**
    *   每月 10 美元 (或每年 100 美元)。
    *   **無限制** 的 agent mode, chat 和 completions。
    *   可使用更多模型 (如 Claude 3.7 Sonnet, o1)。
    *   提供比免費方案多 6 倍的 premium requests。
    *   **針對已驗證的學生、教師和熱門開源專案維護者免費！**
*   **Pro+ (進階專業版):**
    *   每月 39 美元 (或每年 390 美元)。
    *   包含 Pro 的所有功能。
    *   可使用所有模型 (包括 GPT-4.5)。
    *   提供比免費方案多 30 倍的 premium requests。

**對於學生和教師來說，最有吸引力的是可以免費使用 Pro 版本！**

## 申請步驟 (以學生/教師免費 Pro 版本為例)

1.  **準備 GitHub 帳號:**
    *   您需要一個 GitHub 帳號。如果沒有，請先至 [https://github.com/](https://github.com/) 註冊。

2.  **前往 GitHub Copilot 頁面:**
    *   瀏覽至 [https://github.com/features/copilot](https://github.com/features/copilot)。

3.  **選擇方案:**
    *   向下捲動到 "Take flight with GitHub Copilot" 的 Pricing plans 區塊。
    *   點擊 "Pro" 方案下方的連結 (通常是 "Try for 30 days free" 或類似按鈕)。
    *   如果您是學生或教師，GitHub 通常會引導您進行身份驗證。

4.  **學生/教師身份驗證 (重要):**
    *   如果您是學生或教師，並希望申請免費的 Pro 版本，您需要進行身份驗證。
    *   GitHub 通常會與 [GitHub Education](https://education.github.com/) 整合。您可能需要提供學校的電子郵件地址、學生證或其他證明文件。
    *   按照 GitHub 網站上的指示完成驗證流程。這可能需要一些時間等待審核。
    *   **提示:** 尋找頁面上是否有關於 "verified students, teachers, and maintainers of popular open source projects" 免費資格的說明或連結。

5.  **驗證成功或選擇付費/免費試用:**
    *   **如果學生/教師驗證成功：** 您應該可以免費啟用 Copilot Pro。
    *   **如果無法進行學生/教師驗證，或暫時不想驗證：**
        *   您可以選擇開始 **Pro 版本的 30 天免費試用** (需要提供付款資訊，試用期後會自動收費，請注意取消訂閱的時間)。
        *   或者，您可以選擇使用 **Free (免費方案)**，點擊 "Get started" 按鈕即可開始，無需付款資訊，但功能受限。

6.  **授權與設定:**
    *   按照畫面指示完成授權和基本設定。

## 在 VS Code 中啟用 GitHub Copilot

1.  **安裝 VS Code 擴充套件:**
    *   開啟 VS Code。
    *   點擊左側活動列的「擴充套件」圖示。
    *   搜尋 "GitHub Copilot"。
    *   找到由 Microsoft 發布的 **GitHub Copilot** 和 **GitHub Copilot Chat** 擴充套件，點擊 "Install" 安裝。 (通常安裝 GitHub Copilot 會建議一起安裝 Chat)。
    *   **如果您使用 WSL：** 請確保您是在連接到 WSL 的 VS Code 視窗中安裝這些擴充套件 (選擇 "Install in WSL: ...")。

2.  **登入 GitHub 帳號:**
    *   安裝完成後，VS Code 通常會在右下角提示您登入 GitHub 帳號以啟用 Copilot。
    *   點擊提示，或按下 `Ctrl+Shift+P` 開啟命令選擇區，輸入 "GitHub Copilot: Login" 並執行。
    *   依照瀏覽器彈出的指示完成 GitHub 帳號授權。

3.  **開始使用:**
    *   登入成功後，VS Code 編輯器右下角狀態列會顯示 Copilot 的圖示。
    *   現在當您在編輯器中編寫程式碼或註解時，Copilot 就會開始提供建議了！您可以按 `Tab` 鍵接受建議。
    *   您也可以使用 Copilot Chat (通常在左側活動列會有圖示) 來透過對話方式提問、解釋程式碼、生成程式碼等。

---

您現在已經成功申請並設定好 GitHub Copilot。開始享受 AI 輔助編程的便利吧！記得善用學生/教師的免費 Pro 方案資格。 