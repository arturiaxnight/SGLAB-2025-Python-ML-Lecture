# -*- coding: utf-8 -*-
"""
L2_Control_Flow_Exercises.md - 回家作業解答範例
"""

import random # 用於練習三

# %% --- 練習一：初步症狀篩檢分流建議 --- 
print("--- 練習一：初步症狀篩檢分流建議 ---")

def get_triage_recommendation():
    """獲取並驗證篩檢得分，然後提供分流建議。"""
    while True:
        try:
            score_str = input("請輸入初步情緒篩檢得分 (0-6)：")
            score = int(score_str) # 嘗試轉換為整數
            if 0 <= score <= 6:
                break # 輸入有效，跳出迴圈
            else:
                print("輸入無效，得分必須在 0 到 6 之間。請重新輸入。")
        except ValueError:
            print("輸入無效，請輸入一個數字。請重新輸入。")

    recommendation = ""
    if score <= 1:
        recommendation = "情緒狀況相對穩定，建議常規關懷，可預約一個月後追蹤。"
    elif score <= 3:
        recommendation = "輕度情緒困擾，建議安排兩週內諮詢。"
    elif score <= 5:
        recommendation = "中度情緒困擾，建議安排一週內諮詢，並考慮進一步評估。"
    else: # score == 6
        recommendation = "重度情緒困擾，建議立即安排專業評估與介入。"
    
    print(f"初步建議：{recommendation}")

# 執行練習一
get_triage_recommendation()
print("練習一作答完畢。\n")


# %% --- 練習二：藥物遵囑性追蹤與提醒 --- 
print("--- 練習二：藥物遵囑性追蹤與提醒 ---")

def track_medication_adherence():
    """追蹤7天藥物遵囑性並提供回饋。"""
    non_adherent_days = 0
    days_in_week = 7

    print("追蹤過去7天的服藥情況：")
    for i in range(1, days_in_week + 1):
        while True:
            response = input(f"第 {i} 天是否按時服藥 (yes/no): ").strip().lower()
            if response in ["yes", "no", "y", "n"]:
                if response in ["no", "n"]:
                    non_adherent_days += 1
                break # 輸入有效
            else:
                print("輸入無效，請回答 yes 或 no (或 y/n)。")
    
    feedback = ""
    if non_adherent_days == 0:
        feedback = "本週藥物遵囑性良好，請繼續保持！"
    elif non_adherent_days <= 2:
        feedback = "本週大部分時間能按時服藥，請留意並盡量確保每日服藥。"
    else:
        feedback = "本週有數日未按時服藥，這可能會影響治療效果。建議與醫師討論如何改善服藥遵囑性。"
        
    print(f"\n本週未按時服藥天數: {non_adherent_days} 天")
    print(f"回饋：{feedback}")

# 執行練習二
track_medication_adherence()
print("練習二作答完畢。\n")


# %% --- 練習三：簡易睡眠日誌分析與建議 --- 
print("--- 練習三：簡易睡眠日誌分析與建議 ---")

def analyze_sleep_diary():
    """記錄並分析一週睡眠日誌，提供建議。"""
    total_sleep_hours = 0
    days_in_week = 7
    daily_sleep_hours = []

    print("請輸入過去7天的每日睡眠時長（小時）：")
    for i in range(1, days_in_week + 1):
        while True:
            try:
                hours_str = input(f"第{i}天睡眠時長：")
                hours = float(hours_str)
                if 0 <= hours <= 24:
                    daily_sleep_hours.append(hours)
                    total_sleep_hours += hours
                    break # 輸入有效
                else:
                    print("輸入錯誤，睡眠時長應介於0至24小時之間。請重新輸入。")
            except ValueError:
                print("輸入無效，請輸入數字作為睡眠時長。請重新輸入。")

    average_sleep_hours = total_sleep_hours / days_in_week
    recommendation = ""

    if average_sleep_hours < 6:
        recommendation = "您的平均睡眠時長較短，可能影響身心狀態。建議關注睡眠品質，並考慮諮詢專業意見。"
    elif average_sleep_hours <= 9: # 6 到 9 小時 (含)
        recommendation = "您的平均睡眠時長在建議範圍內。保持良好睡眠習慣有助於維持健康。"
    else: # > 9 小時
        recommendation = "您的平均睡眠時長較長。偶爾補眠是正常的，但若長期如此且伴隨日間精神不佳，建議留意。"

    print(f"\n總睡眠時長：{total_sleep_hours:.1f} 小時")
    print(f"平均每日睡眠時長：{average_sleep_hours:.2f} 小時")
    print(recommendation)

# 執行練習三
analyze_sleep_diary()
print("練習三作答完畢。\n")