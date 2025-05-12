# -*- coding: utf-8 -*-
"""
示範 Python 基本資料型態與操作
根據提供的課程列表
"""
# $pip install jupyter


# %% Intro to Python Data Types
# Python 有多種內建資料型態，主要包含：
# Numbers (數字): int, float
# Sequences (序列): str, list, tuple
# Mappings (映射): dict
# Sets (集合): set
# Booleans (布林): bool (True, False)
# NoneType: None

print("--- Intro to Python Data Types ---")
num_int = 10
num_float = 3.14
text_string = "Hello Python"
my_list = [1, 2, 3]
print(my_list[0]) # 取出列表的第一個元素
list_b = ['a', 'b', 'c']
my_tuple = (4, 5, 6)
my_dict = {"name": "Alice", "age": 30}
print(my_dict["name"])
my_set = {7, 8, 9}
my_bool = True
my_none = None

print(f"Integer: {num_int}, Type: {type(num_int)}")
print(f"Float: {num_float}, Type: {type(num_float)}")
print(f"String: {text_string}, Type: {type(text_string)}")
print(f"List: {my_list}, Type: {type(my_list)}")
print(f"Tuple: {my_tuple}, Type: {type(my_tuple)}")
print(f"Dictionary: {my_dict}, Type: {type(my_dict)}")
print(f"Set: {my_set}, Type: {type(my_set)}")
print(f"Boolean: {my_bool}, Type: {type(my_bool)}")
print(f"NoneType: {my_none}, Type: {type(my_none)}")
print("\n")


# %% Operations for Numbers in Python
print("--- Operations for Numbers in Python ---")
a = 15
b = 4

print(f"{a} + {b} = {a + b}")       # 加法
print(f"{a} - {b} = {a - b}")       # 減法
print(f"{a} * {b} = {a * b}")       # 乘法
print(f"{a} / {b} = {a / b}")       # 除法 (結果為浮點數)
print(f"{a} // {b} = {a // b}")     # 整數除法 (Floor division)
print(f"{a} % {b} = {a % b}")       # 取餘數 (Modulo)
print(f"{a} ** {b} = {a ** b}")     # 次方 (Exponentiation)
print("\n")


# %% Functions for Numbers
print("--- Functions for Numbers ---")
num = -7.89

print(f"abs({num}) = {abs(num)}")             # 絕對值
abs(-9)
print(f"round({num}) = {round(num)}")           # 四捨五入到整數
# round(3.3) => 3
print(f"round({num}, 1) = {round(num, 1)}")   # 四捨五入到小數第一位
print(f"pow(4, 3) = {pow(4, 3)}")             # 次方 (同 4 ** 3)
print(f"max(1, 5, 2) = {max(1, 5, 2)}")       # 最大值
print(f"min(1, 5, 2) = {min(1, 5, 2)}")       # 最小值
print("\n")


# %% Variable and Assignment
print("--- Variable and Assignment ---")
x = 100         # 將 100 賦值給變數 x
# x <= 100
y = x           # 將變數 x 的值賦值給變數 y
# y <= x <= 100
x = 200         # 重新賦值給 x，y 的值不受影響 (因為數字是不可變的)

# result = 3   <= 7
# resutl = 7

print(f"x = {x}")
print(f"y = {y}")

# 多重賦值
a, b, c = 1, 2, 3
print(f"Multiple assignment: a={a}, b={b}, c={c}")
a = 1
b = 2
c = 3

# 交換變數
a, b = b, a
print(f"Swapped: a={a}, b={b}")
print("\n")


# %% String Indexing and Slicing
print("--- String Indexing and Slicing ---")
s = "Hello, World!" # 13個字元的字串
# ["H", "e", "l", "l", "o", ",", " ", "W", "o", "r", "l", "d", "!"]

#   H e l l o ,   W o r l d !
#   0 1 2 3 4 5 6 7 8 9 10 11 12 (索引)

# -3-2-1 (負索引)

print(f"String: {s}")
print(f"s[0] = {s[0]}")         # 第一個字元
print(f"s[7] = {s[7]}")         # 第八個字元
print(f"s[-1]  {s[-1]}")        # 最後一個字元
print(f"s[-5] = {s[-5]}")        # 倒數第五個字元

# 切片 (Slicing) [start:stop:step]
# stop 索引本身不包含在內
s  = "qnap_abce_xyz"
print(s[-3::])

print(f"s[0:5] = {s[0:5]}")     # 從索引 0 到 4 (Hello)
print(f"s[7:12] = {s[7:12]}")    # 從索引 7 到 11 (World)
print(f"s[:5] = {s[:5]}")       # 從頭到索引 4 (Hello)
print(f"s[7:] = {s[7:]}")       # 從索引 7 到結尾 (World!)
print(f"s[:] = {s[:]}")         # 整個字串
print(f"s[::2] = {s[::2]}")     # 每隔一個字元取一個 (Hlo ol!)
print(f"s[::-1] = {s[::-1]}")    # 反轉字串 (!dlroW ,olleH)
print("\n")


# %% String Quotations and Line Changing
print("--- String Quotations and Line Changing ---")

# 單引號和雙引號通常可以互換
str1 = 'This is a string.'
str2 = "This is also a string."
print(str1)
print(str2)

# 如果字串內包含引號，可以交錯使用或使用跳脫字元
str3 = "He said, 'Hello!'"
str4 = 'She replied, "Hi there!"'
'It\'s a beautiful day.'
str5 = 'It\'s a beautiful day.' # 使用 \ 跳脫單引號
str6 = "This is a \"quote\"."    # 使用 \ 跳脫雙引號
print(str3)
print(str4)
print(str5)
print(str6)

# 多行字串 (Triple quotes)
multi_line_str = """This is a
multi-line
string."""
print(multi_line_str)

print("""
這段程式是在做什麼
123
123
123
123
""")

# 換行符 \n
# f"{abd} \n {sdf}"
line_change_str = "First line.\nSecond line."
print(line_change_str)

# 使用 \ 可以在程式碼中換行，但不影響字串本身
long_string = "This is a very long string that might need " \
              "to be split across multiple lines in the code."
print(long_string)
print("\n")


# %% String Method I
print("--- String Method I ---")
text = "  Hello Python World  "

print(f"Original: '{text}'")
print(f"text.upper() = '{text.upper()}'")             # 轉大寫
print(f"text.lower() = '{text.lower()}'")             # 轉小寫
print(f"text.strip() = '{text.strip()}'")             # 去除前後空白
print(f"text.lstrip() = '{text.lstrip()}'")            # 去除開頭空白
print(f"text.rstrip() = '{text.rstrip()}'")            # 去除結尾空白
print(f"text.title() = '{text.title()}'")             # 標題格式 (每個單字首字母大寫)
print(f"text.capitalize() = '{text.capitalize()}'")   # 句首字母大寫
print(f"'hello'.isalpha() = {'hello'.isalpha()}")     # 是否全為字母
print(f"'123'.isdigit() = {'123'.isdigit()}")       # 是否全為數字
print(f"'  '.isspace() = {'  '.isspace()}")       # 是否全為空白
print("\n")


# %% Format, fstring and replace
print("--- Format, fstring and replace ---")
name = "Alice"
age = 30
city = "Taipei"

# .format() 方法 老方法
formatted_str1 = "My name is {}, I am {} years old, and I live in {}."\
                 .format(name, age, city)
print(f".format(): {formatted_str1}")

formatted_str2 = "My name is {n}, I am {a} years old, and I live in {c}."\
                 .format(n=name, a=age, c=city)
print(f".format() with keywords: {formatted_str2}")

# f-string (Formatted String Literals) - 推薦使用
f_string = f"My name is {name}, I am {age} years old, and I live in {city}."
print(f"f-string: {f_string}")

# f-string 內可執行表達式
print(f"f-string with expression: {name} will be {age + 5} in 5 years.")

# .replace() 方法
original = "I like cats, cats are cute."
replaced = original.replace("cats", "dogs") # 取代所有 'cats' 為 'dogs'
print(f"Original: {original}")
print(f"Replaced: {replaced}")

replaced_once = original.replace("cats", "dogs", 1) # 只取代第一個 'cats'
print(f"Replaced once: {replaced_once}")
print("\n")


# %% find, count, startswith, endswith
print("--- find, count, startswith, endswith ---")
text = "python is fun, python is easy."

# .find(substring)
# 返回子字串第一次出現的索引，找不到則返回 -1
print(f"text.find('python') = {text.find('python')}")      # 0
print(text[0:6])
print(f"text.find('is') = {text.find('is')}")           # 7
print(f"text.find('java') = {text.find('java')}")         # -1
print(f"text.find('is', 8) = {text.find('is', 8)}")     # 20 (從索引 8 開始找)

# .count(substring)
# 計算子字串出現的次數
print(f"text.count('python') = {text.count('python')}")   # 2
a = [3,3,4,4,5,5,6,6]
print(f"a.count(3) = {a.count(3)}")                     # 2
print(f"text.count('is') = {text.count('is')}")       # 2
print(f"text.count('o') = {text.count('o')}")         # 2

# .startswith(prefix)
# 檢查字串是否以指定前綴開頭

brain= ["lh_wefoiuwehfoij",
"lh_woeifwoijf",
"rh_woijwoijfeowij",
"rh_owijfewofji"]


print("lh_wefoiuwehfoij" in brain)

text.startswith("lh_") 
print(f"text.startswith('python') = {text.startswith('python')}") # True
print(f"text.startswith('java') = {text.startswith('java')}")   # False

# .endswith(suffix)
# 檢查字串是否以指定後綴結尾
print(f"text.endswith('easy.') = {text.endswith('easy.')}")   # True
print(f"text.endswith('fun') = {text.endswith('fun')}")     # False
print("\n")


# %% Other Rules of Strings
print("--- Other Rules of Strings ---")
# 字串是不可變的 (Immutable)
my_string = "Hello"
# my_string[0] = 'J' # 這會導致 TypeError: 'str' object does not support item assignment
print(f"Original string: {my_string}")
new_string = "J" + my_string[1:] # 需要創建新字串來達到修改效果
# my_string[1:] = ello
print(f"Modified string: {new_string}")

# 字串串接 (+) 與重複 (*)
str_a = "Hello"
str_b = " World"
print(f"Concatenation: {str_a + str_b}")
print(f"Repetition: {str_a * 3}")

# 成員運算符 (in, not in)
print(f"'ell' in str_a = {'ell' in str_a}")     # True
print(f"'xyz' not in str_a = {'xyz' not in str_a}") # True
print("\n")


# %% Intro to Lists
print("--- Intro to Lists ---")
# List 是有序、可變的序列，可以包含不同型態的元素
empty_list = []
int_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, [10, 20]]

print(f"Empty list: {empty_list}")
print(f"Integer list: {int_list}")
print(f"Mixed list: {mixed_list}")

# List 索引和切片 (同 String)
print(f"mixed_list[1] = {mixed_list[1]}")       # 'hello'
print(f"mixed_list[-1] = {mixed_list[-1]}")      # [10, 20]
print(f"mixed_list[0:3] = {mixed_list[0:3]}")    # [1, 'hello', 3.14]
print(f"mixed_list[-1][0] = {mixed_list[-1][0]}") # 10 (取巢狀列表元素)

# List 是可變的 (Mutable)
print(f"Original int_list: {int_list}")
int_list[0] = 100
print(f"Modified int_list: {int_list}")
int_list[1:3] = [200, 300] # 修改切片
print(f"Slice modified int_list: {int_list}")
print("\n")


# %% List Functions I
print("--- List Functions I ---")
numbers = [3, 1, 4, 1, 5, 9, 2]

# len()
print(f"len(numbers) = {len(numbers)}")

# .append(item)
print(f"Original numbers: {numbers}")
numbers.append(6) # 在末尾加入元素
print(f"After append(6): {numbers}")

# .insert(index, item)
numbers.insert(0, 0) # 在索引 0 處插入 0
print(f"After insert(0, 0): {numbers}")

# .extend(iterable)
numbers.extend([7, 8]) # 將另一個可迭代物件的元素加入末尾
print(f"After extend([7, 8]): {numbers}")

# .remove(item)
numbers.remove(1) # 移除第一個出現的值為 1 的元素
print(f"After remove(1): {numbers}")

# .pop(index=-1)
last_element = numbers.pop() # 移除並返回末尾元素
print(f"Popped last element: {last_element}, List after pop: {numbers}")
first_element = numbers.pop(0) # 移除並返回索引 0 的元素
print(f"Popped first element: {first_element}, List after pop(0): {numbers}")

# .sort()
numbers.sort() # 原地排序 (升序)
print(f"After sort(): {numbers}")
numbers.sort(reverse=True) # 原地排序 (降序)
print(f"After sort(reverse=True): {numbers}")

# .reverse()
numbers.reverse() # 原地反轉
print(f"After reverse(): {numbers}")

# .index(item)
print(f"numbers.index(9) = {numbers.index(9)}") # 查找 9 的索引
# print(f"numbers.index(100)") # 若找不到會報 ValueError

# .count(item)
print(f"numbers.count(4) = {numbers.count(4)}") # 計算 4 出現的次數
print("\n")


# %% Intro to dicts
print("--- Intro to dicts ---")
# Dictionary (字典) 是無序 (Python 3.7+ 有序)、可變的鍵值對 (key-value pair) 集合
# Key 必須是唯一的且不可變的型態

empty_dict = {}
student = {
    "name": "Bob",
    "age": 25,
    "major": "Computer Science",
    "courses": ["Math", "Physics"],
    "contact": {"email": ["bob@example.com","bob2@example.com"]}
}

print(student['contact']['email'][0]) # 取出聯絡資訊的 email
print(student["courses"][1]) # 取出第一門課程


#%%
#classes = [student, student, student]
classes = []
for i in range(3):
    classes.append(
        {"name": f"Student {i+1}",
            "age": 20 + i,
            "major": "Computer Science",
            "courses": ["Math", "Physics"],
        }
    )

print(classes)
classes[0]["name"] = "Alice"
print(classes)

#%%

print(f"Empty dictionary: {empty_dict}")
print(f"Student dictionary: {student}")

# 存取值 (Accessing values)
print(f"Student's name: {student['name']}")
print(f"Student's age: {student['age']}")
print(f"Student's first course: {student['courses'][0]}")
print(f"Student's email: {student['contact']['email']}")

# 使用 .get() 方法存取 (找不到時不會報錯，返回 None 或指定預設值)
print(f"Student's major: {student.get('major')}")
print(f"Student's phone: {student.get('phone')}") # None
print(f"Student's phone (default): {student.get('phone', 'N/A')}") # N/A

# 修改值 (Modifying values)
student['age'] = 26
print(f"Updated student age: {student['age']}")

# 新增鍵值對 (Adding key-value pairs)
student['city'] = 'New York'
print(f"Added city: {student}")

student["grade"] = 0
print("\n")


# %% Dicts Functions
print("--- Dicts Functions ---")
student = {
    "name": "Charlie",
    "age": 22,
    "major": "Engineering"
}

# len()
print(f"len(student) = {len(student)}")

# .keys()
# 返回一個包含所有鍵的視圖物件 (dict_keys)
print(f"student.keys() = {student.keys()}")
print(f"List of keys: {list(student.keys())}")

# .values()
# 返回一個包含所有值的視圖物件 (dict_values)
print(f"student.values() = {student.values()}")
print(f"List of values: {list(student.values())}")

# .items()
# 返回一個包含所有 (鍵, 值) 元組的視圖物件 (dict_items)
print(f"student.items() = {student.items()}")
print(f"List of items: {list(student.items())}")

# 迭代字典
print("Iterating through keys:")
for key in student:
    print(f"  {key}: {student[key]}")

print("Iterating through items:")
for key, value in student.items():
    print(f"  {key} -> {value}")

# .pop(key, default=None)
# 移除指定鍵並返回其值，若鍵不存在且未提供預設值則報錯
major = student.pop("major")
print(f"Popped major: {major}, Dictionary after pop: {student}")
# non_existent = student.pop("country") # KeyError
non_existent = student.pop("country", "Not Found") # 返回預設值
print(f"Popped non-existent key with default: {non_existent}")

# .popitem()
# 移除並返回最後插入的 (鍵, 值) 對 (Python 3.7+)。在舊版本中，移除隨機對。
last_item = student.popitem()
print(f"Popped item: {last_item}, Dictionary after popitem: {student}")

# .update(other_dict or iterable)
# 用另一個字典或鍵值對序列更新字典
student.update({"age": 23, "city": "London"})
print(f"After update: {student}")

# .clear()
student.clear()
print(f"After clear: {student}")
print("\n")

# 下周從這裡開始

# %% What can be a key?
print("--- What can be a key? ---")
# 字典的鍵必須是不可變 (Immutable) 的資料型態
# 常見的不可變型態：int, float, bool, string, tuple
# 可變型態 (list, dict, set) 不能作為鍵

valid_keys_dict = {
    1: "Integer key",
    3.14: "Float key",
    True: "Boolean key",
    "hello": "String key",
    (1, 2): "Tuple key"
}
print(f"Dictionary with valid keys: {valid_keys_dict}")
print(f"Accessing tuple key: {valid_keys_dict[(1, 2)]}")

# 無效的鍵 (會導致 TypeError)
# invalid_keys_dict = {
#     [1, 2]: "List key"  # TypeError: unhashable type: 'list'
# }
# invalid_keys_dict = {
#     {"a": 1}: "Dict key" # TypeError: unhashable type: 'dict'
# }
print("Lists, dicts, and sets cannot be dictionary keys because they are mutable.")
print("\n")


# %% Intro to Tuples
print("--- Intro to Tuples ---")
# Tuple (元組) 是有序、不可變 (Immutable) 的序列，用小括號 () 表示

empty_tuple = ()
single_element_tuple = (1,) # 注意要有逗號！沒有逗號 (1) 會被視為整數 1
my_tuple = (1, "apple", 3.14, True)

print(f"Empty tuple: {empty_tuple}")
print(f"Single element tuple: {single_element_tuple}, Type: {type(single_element_tuple)}")
print(f"Not a tuple: {(1)}, Type: {type((1))}")
print(f"My tuple: {my_tuple}")

# Tuple 索引和切片 (同 String 和 List)
print(f"my_tuple[1] = {my_tuple[1]}")
print(f"my_tuple[-1] = {my_tuple[-1]}")
print(f"my_tuple[0:2] = {my_tuple[0:2]}")

# Tuple 是不可變的
# my_tuple[0] = 100 # TypeError: 'tuple' object does not support item assignment

# Tuple 常見用途：函數返回多個值、作為字典的鍵
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(f"Coordinates: x={x}, y={y}")
print("\n")


# %% Tuple Packing and Unpacking
print("--- Tuple Packing and Unpacking ---")

# Packing (打包): 將多個值組合成一個 Tuple
packed_tuple = 1, 2, "hello" # 小括號可以省略
print(f"Packed tuple: {packed_tuple}, Type: {type(packed_tuple)}")

# Unpacking (解包): 將 Tuple 中的元素分配給多個變數
# 變數數量必須與 Tuple 元素數量完全匹配
a, b, c = packed_tuple
print(f"Unpacked: a={a}, b={b}, c={c}")

# 如果數量不匹配會導致 ValueError
# x, y = packed_tuple # ValueError: too many values to unpack (expected 2)
# x, y, z, w = packed_tuple # ValueError: not enough values to unpack (expected 4, got 3)

# 使用 * 來解包部分元素 (Python 3+)
numbers = (1, 2, 3, 4, 5)
first, second, *rest = numbers
print(f"Unpacking with *: first={first}, second={second}, rest={rest}")

first, *middle, last = numbers
print(f"Unpacking with *: first={first}, middle={middle}, last={last}")

# 在函數參數中使用
def process_data(id, name, *scores):
    print(f"ID: {id}")
    print(f"Name: {name}")
    print(f"Scores: {scores}") # scores 會是一個 tuple

process_data(101, "David", 90, 85, 92)
print("\n")


# %% Mutable objects in tuples
print("--- Mutable objects in tuples ---")
# Tuple 本身是不可變的，意味著你不能改變 Tuple 中的元素引用
# 但是，如果 Tuple 中的元素是可變物件 (如 List)，則該物件本身可以被修改

mutable_in_tuple = (1, 2, [3, 4])
print(f"Original tuple: {mutable_in_tuple}")

# 不能改變 Tuple 中的元素引用
# mutable_in_tuple[0] = 100 # TypeError
# mutable_in_tuple[2] = [5, 6] # TypeError

# 但可以修改 Tuple 內部可變物件的內容
mutable_in_tuple[2].append(5)
mutable_in_tuple[2][0] = 30
print(f"Tuple after modifying internal list: {mutable_in_tuple}")

# 這個特性使得包含可變物件的 Tuple 不能作為字典的鍵
# invalid_key_tuple = ([1, 2], 3) # TypeError: unhashable type: 'list'
# my_dict = {invalid_key_tuple: "value"}
print("Tuples containing mutable objects cannot be dictionary keys.")
print("\n")


# %% Built-in Set Methods
print("--- Built-in Set Methods ---")
# Set (集合) 是無序、不重複元素的集合，用大括號 {} 表示
# 集合主要用於成員測試和消除重複元素

empty_set = set() # 注意：{} 創建的是空字典
set1 = {1, 2, 3, 4, 4, 5} # 重複的 4 會被自動移除
set2 = {4, 5, 6, 7}
list_with_duplicates = [1, 1, 2, 3, 3, 3, 4]
set_from_list = set(list_with_duplicates)

print(f"Empty set: {empty_set}")
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Set from list: {set_from_list}")

# 集合操作 (數學運算)
# Union (聯集) | 或 .union()
print(f"Union (set1 | set2): {set1 | set2}")
print(f"Union (set1.union(set2)): {set1.union(set2)}")

# Intersection (交集) & 或 .intersection()
print(f"Intersection (set1 & set2): {set1 & set2}")
print(f"Intersection (set1.intersection(set2)): {set1.intersection(set2)}")

# Difference (差集) - 或 .difference()
print(f"Difference (set1 - set2): {set1 - set2}") # 屬於 set1 但不屬於 set2
print(f"Difference (set2 - set1): {set2 - set1}") # 屬於 set2 但不屬於 set1
print(f"Difference (set1.difference(set2)): {set1.difference(set2)}")

# Symmetric Difference (對稱差集) ^ 或 .symmetric_difference()
# (屬於 set1 或 set2，但不同時屬於兩者)
print(f"Symmetric Difference (set1 ^ set2): {set1 ^ set2}")
print(f"Symmetric Difference (set1.symmetric_difference(set2)): {set1.symmetric_difference(set2)}")

# 集合方法
set1.add(6) # 新增元素
print(f"After add(6): {set1}")
set1.update({7, 8}) # 新增多個元素
print(f"After update({{7, 8}}): {set1}")

set1.remove(8) # 移除元素，若元素不存在則報 KeyError
print(f"After remove(8): {set1}")
# set1.remove(10) # KeyError

set1.discard(7) # 移除元素，若元素不存在則忽略
print(f"After discard(7): {set1}")
set1.discard(10) # 不會報錯
print(f"After discard(10): {set1}")

popped_element = set1.pop() # 隨機移除並返回一個元素
print(f"Popped element: {popped_element}, Set after pop: {set1}")

set1.clear() # 清空集合
print(f"After clear: {set1}")

# 子集與超集
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(f"set_a.issubset(set_b) = {set_a.issubset(set_b)}")   # True
print(f"set_b.issuperset(set_a) = {set_b.issuperset(set_a)}") # True
print("\n")


# %% Booleans in Python
print("--- Booleans in Python ---")
# Boolean (布林) 型態只有兩個值：True 和 False

is_active = True
is_greater = 10 > 5
has_permission = False

print(f"is_active: {is_active}, Type: {type(is_active)}")
print(f"is_greater (10 > 5): {is_greater}")
print(f"has_permission: {has_permission}")

# 布林運算 (and, or, not)
print(f"True and False = {True and False}") # False
print(f"True or False = {True or False}")   # True
print(f"not True = {not True}")           # False
print(f"not False = {not False}")         # True

# 任何非零數字、非空序列/映射/集合都被視為 True
# 零、空序列/映射/集合、None 被視為 False
print(f"bool(0) = {bool(0)}")       # False
print(f"bool(1) = {bool(1)}")       # True
print(f"bool(-1) = {bool(-1)}")      # True
print(f"bool('') = {bool('')}")     # False
print(f"bool('abc') = {bool('abc')}") # True
print(f"bool([]) = {bool([])}")     # False
print(f"bool([1]) = {bool([1])}")   # True
print(f"bool({{}}) = {bool({})}")    # False (Empty dict)
print(f"bool(set()) = {bool(set())}") # False (Empty set)
print(f"bool(None) = {bool(None)}")   # False

# 常用於條件判斷
if is_active:
    print("User is active.")
else:
    print("User is inactive.")
print("\n")


# %% Python Comments and Type-checking
print("--- Python Comments and Type-checking ---")

# 單行註解以 '#' 開頭
# This is a single-line comment

x = 10 # 這也是一個行內註解

# 多行註解可以使用多個 '#' 或使用多行字串 (但後者通常用於 docstrings)
# Line 1
# Line 2

"""
This is a multi-line string often used as a docstring
for functions, classes, or modules.
It can also serve as a multi-line comment,
but it's technically a string literal.
"""

# Type Hinting (型態提示) - Python 3.5+
# 幫助靜態分析工具 (如 mypy) 檢查型態，並提高程式碼可讀性
# 它們不會在執行時強制執行型態檢查 (除非使用特殊工具)

def add(a: int, b: int) -> int:
    """This function adds two integers and returns an integer."""
    return a + b

result: int = add(5, 3)
print(f"Type hint example: add(5, 3) = {result}")

name: str = "Eve"
pi: float = 3.14159
items: list[str] = ["apple", "banana"]
data: dict[str, int] = {"a": 1, "b": 2}

# 使用 isinstance() 進行執行時型態檢查
print(f"isinstance(result, int) = {isinstance(result, int)}")     # True
print(f"isinstance(name, str) = {isinstance(name, str)}")       # True
print(f"isinstance(items, list) = {isinstance(items, list)}")     # True
print(f"isinstance(pi, float) = {isinstance(pi, float)}")       # True
print(f"isinstance(data, dict) = {isinstance(data, dict)}")       # True
print(f"isinstance(result, str) = {isinstance(result, str)}")     # False
print("\n")


# %% Additional Information
print("--- Additional Information ---")

# %% Value vs Reference
# Python 中的賦值行為

# 對於不可變物件 (int, float, str, tuple, bool, None):
# 賦值是傳遞「值」的副本 (或更精確地說，是引用的副本，但因為不可變，效果類似傳值)
x = 10
y = x
y = 20 # 修改 y 不會影響 x
print(f"Immutable: x={x}, y={y}")

tup1 = (1, 2)
tup2 = tup1
# tup2[0] = 100 # TypeError, tuple is immutable
tup2 = (3, 4) # tup2 現在引用一個新的 tuple 物件，tup1 不變
print(f"Immutable Tuple: tup1={tup1}, tup2={tup2}")

# 對於可變物件 (list, dict, set):
# 賦值是傳遞「引用」
list1 = [1, 2, 3]
list2 = list1 # list1 和 list2 指向同一個 list 物件
list2.append(4) # 修改 list2 會影響 list1，因為它們指向同一個物件
print(f"Mutable List: list1={list1}, list2={list2}")

# 如果想複製列表 (淺拷貝 - shallow copy)
list3 = list1.copy() # 或 list3 = list1[:]
list3.append(5)
print(f"Shallow Copy: list1={list1}, list3={list3}") # list1 不受影響

# 注意淺拷貝的限制：如果列表內還有可變物件，它們仍然共享引用
list_a = [1, [10, 20]]
list_b = list_a.copy()
list_b[0] = 100       # 不影響 list_a
list_b[1].append(30) # 會影響 list_a，因為內部列表是共享的
print(f"Shallow Copy Nested: list_a={list_a}, list_b={list_b}")

# 深拷貝 (deep copy) - 需要 import copy 模組
import copy
list_c = copy.deepcopy(list_a)
list_c[1].append(40)
print(f"Deep Copy: list_a={list_a}, list_c={list_c}") # list_a 不受影響


# %% sorted() function
# sorted() 是一個內建函數，可以對任何可迭代物件進行排序，並返回一個新的排序後的列表
# 它不會修改原始的可迭代物件
numbers_to_sort = [3, 1, 4, 1, 5, 9, 2]
string_to_sort = "python"
tuple_to_sort = (6, 2, 8, 1)

sorted_numbers = sorted(numbers_to_sort)
sorted_string_chars = sorted(string_to_sort)
sorted_tuple = sorted(tuple_to_sort)

print(f"Original numbers: {numbers_to_sort}")
print(f"Sorted numbers (new list): {sorted_numbers}")
print(f"Original numbers unchanged: {numbers_to_sort}")

print(f"Original string: {string_to_sort}")
print(f"Sorted string characters: {sorted_string_chars}")

print(f"Original tuple: {tuple_to_sort}")
print(f"Sorted tuple elements: {sorted_tuple}")

# 降序排序
sorted_numbers_desc = sorted(numbers_to_sort, reverse=True)
print(f"Sorted numbers descending: {sorted_numbers_desc}")

# sorted() vs .sort()
# sorted() 返回新列表，不改變原物件
# .sort() 是列表的方法，原地修改列表，返回 None
original_list = [5, 2, 9]
new_sorted_list = sorted(original_list)
original_list.sort()
print(f"sorted() result: {new_sorted_list}")
print(f".sort() modifies original: {original_list}")


# %% Membership Operator (in, not in)
# 用於檢查某個元素是否存在於序列 (string, list, tuple) 或集合 (set, dict keys) 中

my_list = [10, 20, 30, 40]
my_string = "Hello World"
my_tuple = (1, 2, 3)
my_set = {'a', 'b', 'c'}
my_dict = {'x': 1, 'y': 2}

# List
print(f"20 in my_list = {20 in my_list}")       # True
print(f"50 not in my_list = {50 not in my_list}") # True

# String
print(f"'World' in my_string = {'World' in my_string}") # True
print(f"'world' in my_string = {'world' in my_string}") # False (大小寫敏感)
print(f"'ell' in my_string = {'ell' in my_string}")   # True

# Tuple
print(f"1 in my_tuple = {1 in my_tuple}")         # True

# Set
print(f"'a' in my_set = {'a' in my_set}")         # True
print(f"'d' not in my_set = {'d' not in my_set}")   # True

# Dictionary (檢查的是鍵)
print(f"'x' in my_dict = {'x' in my_dict}")         # True
print(f"1 in my_dict = {1 in my_dict}")           # False (檢查鍵，不是值)
print(f"'y' not in my_dict = {'y' not in my_dict}")   # False

# 檢查值是否存在於字典中
print(f"1 in my_dict.values() = {1 in my_dict.values()}") # True

print("\nEnd of Demo")

# %%
