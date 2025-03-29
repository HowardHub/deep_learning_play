"""
    
    dict.get(key, 'default_reutan_value') get()函数的应用
    dict_new = {**dict1, **dict2} 合并两个字典
    exchanged_dict = {v: k for k, v in original.items()} 交换key-value
    max_name, max_score = max(students.items(), key=lambda x: x[1]) 
"""



"""
第一题：
    1.创建一个字典 person，包含以下键值对：
	2.	打印 person 字典的 姓名 和 职业。
	3.	让用户输入一个键（如 “年龄”），输出该键对应的值。
	•	如果键不存在，提示 "键不存在"。
"""
person = {
    "姓名": "张三",
    "年龄": 25,
    "职业": "程序员"
}
print(f'姓名：{person["姓名"]}, 职业：{person["职业"]}')
key = input('请输入要查询的内容：')
if key in person:
    print(person[key])
else:
    print('键不存在')
print(person.get(key, '键不存在'))

# 优化版本：print(person.get(key, "键不存在"))




"""
第二题：
	1.	创建一个字典 student，包含以下信息：
    2.	给字典添加一个键值对："性别": "男"。
	3.	修改 "成绩" 为 90。
	4.	删除 "班级" 这个键。
	5.	输出最终字典。
"""
student = {
    "姓名": "李四",
    "班级": "高三(2)班",
    "成绩": 85
}

student['性别'] = '男'
student['成绩'] = 90
del student["班级"]
print(student)




"""
题目 3：统计单词出现次数
	1.	让用户输入一句话，例如 "hello world hello python"。
	2.	统计每个单词出现的次数，并存入字典中，例如：
    3.	打印字典。
"""
words = input("请输入一句话：")
lst = words.split(' ') #默认按空格分割
single_set = set(lst)
word_dict = {}
for word in single_set:
    word_dict[word] = lst.count(word)
print(word_dict)



# ✅ 你的思路是对的，但 不需要先转换成 set 再遍历，因为 set 不能保证原顺序。可以直接用 dict 计数：
"""
⚡ 优化点：
	•	直接遍历 words.split()，少一次 set 转换。
	•	word_dict.get(word, 0) + 1 避免 KeyError，更优雅。
"""
words = input("请输入一句话：")
word_dict = {}
for word in words.split():  # split() 默认按空格分割
    # get()的第二个参数是，如果查询不到，则返回默认值，这里表示查询不到，返回0
    word_dict[word] = word_dict.get(word, 0) + 1
print(word_dict)





"""
📌 题目 4：遍历字典
	1.	创建一个字典 scores，表示不同学生的分数：
    2.	使用 for 循环遍历字典：
	    •	逐行打印 "学生: 分数" 格式，例如 "张三: 90"。

"""
scores = {
    "张三": 90,
    "李四": 85,
    "王五": 78,
    "赵六": 92
}
for name, score in scores.items(): # 记得是scores.items()，而不是scores
    print(f'{name}:{score}')



"""
📌 题目 5：合并两个字典
	1.	创建两个字典：
    2.	合并 dict1 和 dict2，并输出合并后的字典。
"""
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}
dict3 = {}
for key, value in dict1.items():
    dict3[key] = value
for key, value in dict2.items():
    dict3[key] = value
print(dict3)
# print({**dict1, **dict2})

# 更简洁的方式：dict3 = {**dict1, **dict2}

# 或者
# dict3 = dict1.copy()  
# dict3.update(dict2) 



"""
📌 题目 6：找出最高分
	1.	给定一个字典 students，其中存储了多个学生的成绩：
    2.	找出最高分，并打印对应的学生姓名和分数。
"""
students = {
    "张三": 78,
    "李四": 88,
    "王五": 95,
    "赵六": 85
}
max_name = ''
max_score = 0
for name, score in students.items():
    if score > max_score:
        max_score = score
        max_name = name
print(f'最高分姓名：{max_name}，成绩：{max_score}')
# 更简洁的方式：max_name, max_score = max(students.items(), key=lambda x: x[1])
# max(students.items(), key=lambda x: x[1]) 直接找出最高分，不需要手动遍历。

# students.items() 将字典转换为可迭代的键值对元组，形式如 [("张三",78), ("李四",88), ...]
# key=lambda x: x[1] 指定比较的依据是每个元组的第二个元素（即成绩）





"""
📌 题目 7：交换字典的键和值
	1.	给定一个字典：
    2.	交换键和值，变成：
    3.	输出转换后的字典。
"""
original = {"apple": "苹果", "banana": "香蕉", "grape": "葡萄"}
print(f'交换前的字典：{original}')
exchanged_dict = {}
for key, value in original.items():
    exchanged_dict[value] = key
print(f'交换后的字典：{exchanged_dict}')

# 更简洁的方式exchanged_dict = {v: k for k, v in original.items()}