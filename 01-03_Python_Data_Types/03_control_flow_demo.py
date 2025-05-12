# -*- coding: utf-8 -*-
"""
示範 Python 的判斷式 (if/else) 與迴圈 (for/while)
根據 README.md Lesson 2 的內容
"""

# %% --- 判斷式 (Conditional Statements) ---
print("--- 判斷式 (Conditional Statements) ---")

# %% 基本 if 敘述
print("\n--- 基本 if 敘述 ---")
x = 10
if x > 5:
    print(f"{x} 大於 5")

temperature = 30
if temperature > 28:
    print("天氣炎熱，建議開冷氣。")

# %% if-else 敘述
print("\n--- if-else 敘述 ---")
y = 3
if y % 2 == 0:
    print(f"{y} 是偶數")
else:
    print(f"{y} 是奇數")

age = 18
if age >= 20:
    print("您是成年人。")
else:
    print("您是未成年人。")

# %% if-elif-else 敘述
print("\n--- if-elif-else 敘述 ---")
score = 85
if score >= 90:
    print("等級 A")
elif score >= 80:
    print("等級 B")
elif score >= 70:
    print("等級 C")
elif score >= 60:
    print("等級 D")
else:
    print("等級 F (不及格)")

# %% 巢狀 if 敘述 (Nested if)
print("\n--- 巢狀 if 敘述 ---")
num = 15
if num > 0:
    print(f"{num} 是正數")
    if num % 2 == 0:
        print(f"{num} 也是偶數")
    else:
        print(f"{num} 是奇數")
elif num == 0:
    print(f"{num} 是零")
else:
    print(f"{num} 是負數")

# %% 條件表達式 (Conditional Expressions / Ternary Operator)
print("\n--- 條件表達式 (Ternary Operator) ---")
z = 7
result = "偶數" if z % 2 == 0 else "奇數"
print(f"{z} 是 {result}")

is_member = True
fee = 50 if is_member else 100
print(f"費用: {fee}")
print("\n")


# %% --- 迴圈 (Loops) ---
print("--- 迴圈 (Loops) ---")

# %% for 迴圈 (For Loops)
print("\n--- for 迴圈 ---")

# 迭代序列 (串列 List)
print("迭代串列:")
fruits = ["蘋果", "香蕉", "櫻桃"]
for fruit in fruits:
    print(fruit)

# 迭代序列 (字串 String)
print("\n迭代字串:")
for char in "Python":
    print(char)

# 迭代序列 (元組 Tuple)
print("\n迭代元組:")
colors = ("紅", "綠", "藍")
for color in colors:
    print(color)

# 使用 range() 函數
print("\n使用 range():")
print("range(5):")
for i in range(5): # 從 0 到 4
    print(i)

print("\nrange(2, 6):")
for i in range(2, 6): # 從 2 到 5
    print(i)

print("\nrange(1, 10, 2):")
for i in range(1, 10, 2): # 從 1 到 9，間隔 2
    print(i)

# %% for 迴圈中的 break 和 continue
print("\n--- for 迴圈中的 break 和 continue ---")

print("使用 break:")
for i in range(1, 10):
    if i == 5:
        print("遇到 5，跳出迴圈")
        break
    print(i)

print("\n使用 continue:")
for i in range(1, 6):
    if i == 3:
        print("遇到 3，跳過此次迭代")
        continue
    print(i)

# %% for 迴圈的 else 子句
# 當迴圈正常結束 (沒有被 break 中斷) 時執行
print("\n--- for 迴圈的 else 子句 ---")
for i in range(3):
    print(f"迭代 {i}")
else:
    print("迴圈正常結束")

print("\n有 break 的 for 迴圈:")
for i in range(3):
    print(f"迭代 {i}")
    if i == 1:
        print("以 break 中斷")
        break
else:
    print("迴圈正常結束 (此處不會執行)")


# %% while 迴圈 (While Loops)
print("\n--- while 迴圈 ---")
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1 # 重要：更新條件變數，避免無限迴圈

# %% while 迴圈中的 break 和 continue
print("\n--- while 迴圈中的 break 和 continue ---")
print("使用 break:")
c = 0
while c < 10:
    if c == 5:
        print("遇到 5，跳出迴圈")
        break
    print(c)
    c += 1

print("\n使用 continue:")
c = 0
while c < 5:
    c += 1
    if c == 3:
        print("遇到 3，跳過此次迭代")
        continue
    print(c)

# %% while 迴圈的 else 子句
# 當迴圈條件變為 False (沒有被 break 中斷) 時執行
print("\n--- while 迴圈的 else 子句 ---")
num = 0
while num < 3:
    print(f"數字: {num}")
    num += 1
else:
    print("迴圈正常結束")

print("\n有 break 的 while 迴圈:")
num = 0
while num < 3:
    print(f"數字: {num}")
    if num == 1:
        print("以 break 中斷")
        break
    num += 1
else:
    print("迴圈正常結束 (此處不會執行)")
print("\n")


# %% --- 練習：BMI 計算與體重狀況判斷 ---
print("--- 練習：BMI 計算與體重狀況判斷 ---")
# 說明：讓使用者輸入身高體重，或使用預設資料集進行迴圈處理

# 單次輸入計算
try:
    height_cm_str = input("請輸入您的身高（公分）: ")
    weight_kg_str = input("請輸入您的體重（公斤）: ")

    # 檢查輸入是否為空，若是則提示並跳過
    if not height_cm_str or not weight_kg_str:
        print("身高和體重不可為空。請重新執行並輸入有效值。")
    else:
        height_cm = float(height_cm_str)
        weight_kg = float(weight_kg_str)

        if height_cm <= 0 or weight_kg <= 0:
            print("身高和體重必須是正數。")
        else:
            height_m = height_cm / 100
            bmi = weight_kg / (height_m ** 2)
            print(f"您的 BMI 是: {bmi:.2f}")

            if bmi < 18.5:
                print("體重狀況：過輕")
            elif 18.5 <= bmi < 24:
                print("體重狀況：正常")
            elif 24 <= bmi < 27:
                print("體重狀況：過重")
            elif 27 <= bmi < 30:
                print("體重狀況：輕度肥胖")
            elif 30 <= bmi < 35:
                print("體重狀況：中度肥胖")
            else: # bmi >= 35
                print("體重狀況：重度肥胖")
except ValueError:
    print("輸入無效，請輸入數字。")
except Exception as e:
    print(f"發生錯誤: {e}")

print("\n--- 使用迴圈處理多筆資料 ---")
# 假設我們有一組資料 (姓名, 身高cm, 體重kg)
data_samples = [
    ("小明", 170, 65),
    ("小華", 160, 70),
    ("小美", 155, 45),
    ("大壯", 180, 90),
    ("小莉", 165, "55"), # 包含一個錯誤資料型態的例子
    ("無效", -170, 60), # 包含一個無效數值的例子
    ("空白測試", "", "60") # 包含空白輸入的例子
]

for name, height_cm, weight_kg in data_samples:
    print(f"\n正在計算 {name} 的 BMI...")
    try:
        # 檢查輸入是否為空字串
        if isinstance(height_cm, str) and not height_cm.strip():
            print(f"  {name} 的身高資料為空。跳過計算。")
            continue
        if isinstance(weight_kg, str) and not weight_kg.strip():
            print(f"  {name} 的體重資料為空。跳過計算。")
            continue

        # 型態檢查與轉換
        h_cm = float(height_cm)
        w_kg = float(weight_kg)

        if h_cm <= 0 or w_kg <= 0:
            print(f"  {name} 的身高或體重資料無效 ({h_cm}cm, {w_kg}kg)。跳過計算。")
            continue # 跳過此筆資料

        height_m = h_cm / 100
        bmi = w_kg / (height_m ** 2)
        print(f"  {name} 的 BMI 是: {bmi:.2f}")

        if bmi < 18.5:
            status = "過輕"
        elif 18.5 <= bmi < 24:
            status = "正常"
        elif 24 <= bmi < 27:
            status = "過重"
        elif 27 <= bmi < 30:
            status = "輕度肥胖"
        elif 30 <= bmi < 35:
            status = "中度肥胖"
        else: # bmi >= 35
            status = "重度肥胖"
        print(f"  體重狀況：{status}")

    except ValueError:
        print(f"  {name} 的身高或體重資料格式錯誤 (身高: '{height_cm}', 體重: '{weight_kg}')。跳過計算。")
    except Exception as e:
        print(f"  計算 {name} 的 BMI 時發生未預期錯誤: {e}")

print("\nEnd of Demo") 