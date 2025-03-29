
"""
1.编写一个程序，创建一个包含 5 个水果名称的列表 fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]，然后：
	•	打印列表中的第一个和最后一个元素
	•	让用户输入一个索引值（0-4），输出该索引对应的水果名称。如果索引超出范围，提示“索引超出范围”。
"""

fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
print(f'第一个水果：{fruits[0]}')
print(f'最后一个水果：{fruits[len(fruits) - 1]}') #直接用fruits[-1]来访问最后一个元素

idx = input('输入一个索引值（0-4）')
try:
    if idx.isdigit():
        idx = int(idx)
        if idx < 0 or idx > 4:
            print('索引超出范围')
        else:
            print(f'索引为{idx}，的水果是{fruits[idx]}')
    else:
        print('请输入正整数')
# 不需要 try-except 处理 ValueError，因为 isdigit() 已经过滤掉非数字输入了。
except ValueError:
    print('请输入数字')





"""
2.让用户输入一个整数 N，然后创建一个包含 1 到 N 的整数列表，并执行以下操作：
	•	在列表末尾添加一个数字 N+1
	•	删除列表中的第一个元素
	•	将列表中的最后一个元素改为 999
	•	打印修改后的列表

"""
num = input("请输入一个正整数：")
try:
    if num.isdigit():
        num = int(num)
        if num <= 0:
            print('输入的不是正整数!')
        else:
            lst = list(range(1, num+1))
            print('修改前的列表为')
            print(lst)
            lst.append(num+1)
            del lst[0] # 可改为 lst.pop(0)
            lst[len(lst) - 1] = 999 # 可改为lst[-1] = 999  # 修改最后一个元素，更简洁
            print('修改后的列表为')
            print(lst)
    else:
        print('输入的不是正整数!')
except ValueError:
    print('输入的不是正整数!')




"""
3.让用户输入一串数字（用空格分隔，如 1 2 3 4 5 1 2 1 3 4），将其存入列表，然后：
	•	让用户输入一个要查找的数字，统计它在列表中出现的次数。
"""
num_str = input('请输入一串数字')
numbers = []
for char in num_str:
    numbers.append(int(char))
print(numbers)
key = input('请输入要查找的数字：')
total_sum = 0
try:
    key = int(key)
except ValueError:
    print('输入的不是正整数')

if key < 0 or key > 9:
    print('输入的数字不是0～9')
else:
    for i in numbers:
        if i == key:
            total_sum += 1

    print(f'数字{key}，出现了{total_sum}次')



"""
4.让用户输入多个整数（用空格分隔），存入列表后：
	•找出列表中的最大值和最小值并输出。
"""

num_str = input('输入多个整数（用空格分隔）')
numbers =[]
for a in num_str.split(' '):
    if a.isdigit():
        numbers.append(int(a))
if len(numbers) > 0:
    max_num, min_num = max(numbers), min(numbers)
    print(f'最大值：{max_num}，最小值：{min_num}')




"""
5.让用户输入多个字符串（用空格分隔），存入列表后：
	•	反转列表（不使用 reverse() 方法）。
	•	输出反转后的列表。
"""
strs = input('输入多个字符串（用空格分隔）:')
str_lst = []
for a in strs.split(' '):
    str_lst.append(a)

print(str_lst)
for i in range(len(str_lst) - 1, -1, -1):
    print(str_lst[i])
# 优化反转方式，reversed_list = str_lst[::-1]  # 切片方式更简单