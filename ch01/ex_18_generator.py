
"""
二、生成器
语法
def generator_name():
    yield 值1
    yield 值2
    yield 值3
    # 更多yield...
案例
def odd_numbers():
    n = 1
    while True:   # 无限循环
        yield n
        n += 2



"""





"""
📌 题目 2：简单生成器函数
定义一个名为 count_to_n(n) 的生成器函数，生成从 1 到 n 的整数。
"""
def count_to_n(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# 测试代码
for num in count_to_n(5):
    print(num)






"""
📌 题目 4：使用生成器实现斐波那契数列
定义一个生成器函数 fibonacci_gen(n)，生成前 n 个斐波那契数。
"""
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 测试代码
for num in fibonacci_gen(7):
    print(num, end=' ')



print()




"""
📌 题目 6：生成器实现无限序列（使用 yield）
定义一个无限序列生成器 infinite_counter()，从 1 开始每次递增1，并在调用端手动停止（通过 break）。
"""
def infinite_counter():
    a = 0
    while True:
        yield a
        a += 1


# 测试代码
for num in infinite_counter():
    if num > 5:
        break
    print(num, end=' ')

print()












"""
📌 题目 7：生成器表达式
使用生成器表达式（Generator Expression）定义一个名为 square_gen 的生成器，用于生成从1到5的平方数。
"""

square_gen = (x*x for x in range(1, 6))

# 测试代码
gen = square_gen
for num in gen:
    print(num, end=' ')

print('tst')





"""
📌 题目 8：使用 yield from 迭代嵌套生成器
定义两个生成器函数：
	•	gen1() 生成 1, 2, 3
	•	gen2() 生成 4, 5, 6
再定义一个函数 combined_gen() 使用 yield from 迭代前两个生成器。
"""
def gen1():
    a = 1
    while a <= 3:
        yield a
        a += 1


def gen2():
    b = 4
    while b <= 6:
        yield b
        b += 1


def combined_gen():
    yield from gen1()
    yield from gen2()


# 测试代码
for num in combined_gen():
    print(num, end=' ')



print()






"""
📌 题目 9：用生成器读取文件（模拟）
定义一个生成器函数 read_lines()，用于逐行读取一个模拟的文本列表（作为模拟文件），并在读取每一行时打印 "读取一行数据..."。
"""

def read_lines(mock_file):
    i = 0
    while i < len(mock_file):
        yield f'读取一行数据... {mock_file[i]}'
        i += 1


# 模拟文件内容：
mock_file = [
    '第一行内容',
    '第二行内容',
    '第三行内容'
]

# 测试代码：
for line in read_lines(mock_file):
    print(line)
"""
题目要求每次先打印提示，再返回内容。
"""
def read_lines(mock_file):
    for line in mock_file:
        print("读取一行数据...")
        yield line




"""
📌 题目 10（挑战题）：生成器实现杨辉三角
定义一个生成器函数 yanghui_triangle(n)，生成杨辉三角的前 n 行，每行以列表形式给出。
"""
def yanghui_triangle(n):
    pass

# 测试代码：
for row in yanghui_triangle(5):
    print(row)
