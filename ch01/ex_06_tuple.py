

"""
1.	•	创建一个包含 5 个城市名称的元组 cities = ("北京", "上海", "广州", "深圳", "成都")。
	•	打印元组的第一个和最后一个城市。
	•	让用户输入一个索引值（0-4），输出该索引对应的城市名称，如果索引超出范围，提示 "索引超出范围"。
"""
cities = ('北京', '上海', '广州', '深圳', '成都')
print(f'第一个城市：{cities[0]}')
print(f'最后一个城市：{cities[-1]}')

idx = input('请输入一个索引值（0-4）：')
if idx.isdigit: # 在 第 1 题 和 第 2 题，你使用了 idx.isdigit，但 isdigit 是方法，应该写成 idx.isdigit()
    idx = int(idx)
    if idx >= 0 and idx <= 4:
        print(f'第{idx+1}个城市是：{cities[idx]}')
    else:
        print('索引超出范围')


"""
2.	•	创建一个元组 numbers = (10, 20, 30, 40, 50)。
	•	让用户输入一个索引值 i（0-4），然后尝试修改 numbers[i] = 100，观察 Python 是否会报错，并解释为什么会这样。
"""
numbers = (10, 20, 30, 40, 50)
idx = input('请输入一个索引值（0-4）：')
if idx.isdigit: #在 第 1 题 和 第 2 题，你使用了 idx.isdigit，但 isdigit 是方法，应该写成 idx.isdigit()
    idx = int(idx)
    if idx >= 0 and idx <= 4:
        numbers[idx] = 100 # 会报错，因为元组中的元素是不可变的。
    else:
        print('索引超出范围')




"""
3.	创建一个包含 10 个整数的元组 nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)。
	•	打印前 3 个元素。
	•	打印最后 3 个元素。
	•	打印索引 2 到 7（包含索引 2，不包含索引 7） 的元素。
	•	反转元组并输出。
"""

"""
切片语法：my_tuple[start:stop:step]。其中：
    start: 开始索引（不包含）。
    stop: 结束索引（包含）。
    step: 步长（默认为1）
"""
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'前3个元素：{nums[:3]}')
print(f'后3个元素{nums[-3:]}')
print(f'索引 2 到 7（包含索引 2，不包含索引 7） 的元素:{nums[2:7]}')
print(f'反转元组：{nums[::-1]}') # [::-1]表示从右到左（即反向）取出所有元素，步长为1。



"""
4.	•	创建一个元组 fruits = ("苹果", "香蕉", "橙子", "葡萄", "西瓜")。
	•	使用 for 循环遍历元组，并逐行打印每个水果。
"""
fruits = ("苹果", "香蕉", "橙子", "葡萄", "西瓜")
for fruit in fruits:
    print(fruit)


"""
5.	•	假设有一个元组 person = ("张三", 25, "程序员")，分别表示 姓名、年龄、职业。
	•	使用解包（unpacking）分别提取出 name、age、job，然后打印出来。
"""
person = ("张三", 25, "程序员")
name, age, job = person
print(f'姓名：{name}')
print(f'年龄：{age}')
print(f'职业：{job}')


"""
6.	
    •	创建一个包含多个元组的元组：
    •	打印第二个学生的信息。
	•	打印所有学生的姓名。

"""
students = (
    ("张三", 18, "男"),
    ("李四", 19, "女"),
    ("王五", 17, "男"),
    ("赵六", 20, "女")
)
print(f'第二个学生信息：{students[1]}')
for student in students:
    print(student[0])



"""
7.	•	创建一个元组 animals = ("猫", "狗", "兔子", "老虎")。
	•	将元组转换为列表，然后：
	•	向列表中添加一个新元素 "大象"。
	•	删除 "兔子"。
	•	修改 "老虎" 为 "狮子"。
	•	再转换回元组，并输出结果。

"""
animals = ("猫", "狗", "兔子", "老虎")
lst = list(animals) #用list函数，将元组转为列表
lst.append('大象')
del lst[2] # lst.remove("兔子")  # 删除 "兔子"，如果不存在会报错
lst[2] = '狮子'
animals = tuple(lst) #用tuple函数，将列表转为元组
print(animals)




"""
8.	•	创建一个元组 numbers = (1, 2, 3, 4, 5, 1, 2, 1, 3, 4, 1)。
	•	统计数字 1 在元组中出现的次数。
	•	查找数字 3 在元组中的第一个索引位置。
"""

numbers = (1, 2, 3, 4, 5, 1, 2, 1, 3, 4, 1)
total_count = numbers.count(1)
print(f'数字 1 在元组中出现的次数{total_count}')

first_idx = numbers.index(3)
print(f'数字 3 在元组中的第一个索引位置{first_idx}')

