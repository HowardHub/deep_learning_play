
#List Comprehensions 列表解析
# 基本语法：[expression for item in iterable]
# 作用：用一行代码替代多行for循环
# 第6题不会，第9题作答不规范
"""
matrix = [[1, 2], [3, 4], [5, 6]]

lst = [num for sublist in matrix for num in sublist]
等价于：
lst = []
for sublist in matrix:    # 遍历 matrix 的每一行（子列表）
    for num in sublist:   # 遍历子列表的每个元素
        lst.append(num)   # 将每个元素加入新列表
"""





"""
📌 题目 1：基础列表解析
   •	使用列表解析创建一个列表，包含从 1 到 10 的整数。
   预期输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
lst = [x for x in range(1,11)]
print(lst)


"""
📌 题目 2：平方数列表
	•	使用列表解析创建一个列表，包含从 1 到 10 的整数的 平方。
"""
lst = [x * x for x in range(1, 11)]
print(lst)


"""
📌 题目 3：过滤偶数
	•	使用列表解析创建一个列表，包含从 1 到 20 之间所有的 偶数。
"""
lst = [x for x in range(1,21) if x % 2 == 0]
print(lst)



"""
📌 题目 4：字符串处理
	•	给定一个列表：     
    •	使用列表解析去除每个元素两侧的空格并转为全小写字母。
"""
fruits = [' apple ', 'banana', ' ORANGE ', 'Mango', 'waterMelon ']

lst = [fruit.strip().lower() for fruit in fruits]
print(lst)


"""
📌 题目 5：条件表达式
	•	使用列表解析创建一个列表，将 1 到 10 中的整数转换为对应的字符串：
	•	如果是奇数，转换为 '奇数'；
	•	如果是偶数，转换为 '偶数'。
"""
lst =['偶数' if x % 2 == 0 else '奇数'  for x in range(1, 11)]
print(lst)



"""
📌 题目 6：嵌套列表解析
	•	使用列表解析创建一个 二维列表（矩阵），表示一个 3×3 的单位矩阵（对角线为1，其余为0）。
    预期输出
    [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
"""
matrix = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(matrix)
"""
等价于
matrix =[]
for j in range(3):
    row =[]
    for i in range(3):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)
print(matrix)
"""






"""
📌 题目 7：多个条件过滤
	•	给定一个列表：
    •	使用列表解析提取出列表中同时满足以下两个条件的数字：
	•	大于20；
	•	是偶数。
"""
numbers = [15, 22, 8, 19, 31, 44, 55, 63, 70]
lst = [x for x in numbers if x > 20 and x % 2 == 0]
print(lst)




"""
📌 题目 8：文件名处理
	•	给定一个文件名列表：
    •	使用列表解析提取出所有以 .py 结尾的文件名。

"""
files = ['test.py', 'demo.txt', 'image.png', 'data.csv', 'script.py', 'note.md']
lst = [file for file in files if file.endswith('.py')]
print(lst)





"""
📌 题目 9：二维列表扁平化
	•	给定一个二维列表：
    •	使用列表解析将其转化为一维列表。
    这题蛮有意思！
"""
matrix = [[1, 2], [3, 4], [5, 6]]
lst = [list[i] for list in matrix for i in range(2)]
print(lst)

"""
问题：
	•	你使用了内置关键字 list 作为变量名，这样做虽然不会直接报错，但不是一个好的编程习惯，可能会覆盖内置函数。
	•	你使用了固定的 range(2) 来遍历子列表，虽然在此题正确，但如果子列表长度不一致就会有问题。
    lst = [num for sublist in matrix for num in sublist]

等价于：
lst = []
for sublist in matrix:    # 遍历 matrix 的每一行（子列表）
    for num in sublist:   # 遍历子列表的每个元素
        lst.append(num)   # 将每个元素加入新列表
"""
lst = [num for sublist in matrix for num in sublist]
print(lst)







"""
📌 题目 10：结合字典和列表解析
	•	给定一个字典列表：
	•	使用列表解析提取出所有分数大于或等于80的学生姓名。
"""
students = [
    {'name': '张三', 'score': 85},
    {'name': '李四', 'score': 92},
    {'name': '王五', 'score': 58},
    {'name': '赵六', 'score': 76}
]
names = [student['name']  for student in students if student['score'] > 80] #题目要求>=80
print(names)



