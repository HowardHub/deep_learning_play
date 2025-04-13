import random




print('有趣的for，步长不是1的情况')
for i in range(1, 100, 10):
    print(i)




"""
    1.使用 while 循环打印 1 到 10（每行一个数字）。
"""
i = 1
while i <= 10:
    print(i)
    i += 1


"""
    2.让用户输入一个正整数 N，然后使用 for 循环计算 1 + 2 + ... + N 的总和，并输出结果。
"""
num = input('请输入一个正整数：')
sum = 0
try: 
    num = int(num)
    if num <= 0:
        print('请输入正整数')
except ValueError:
    print('你输入的不是正整数')
i = 1
for i in range(num+1):
    sum = i + sum
print('结果为{}'.format(sum))

"""
问题：
	•	try 语句的 except 只会捕获 ValueError，但如果 num <= 0，不会执行 except，而是继续执行 for 循环，可能会导致错误。
	•	for i in range(num+1): 的 i 会覆盖外面的 i = 1，但 i 在 for 里已经被定义，不需要 i = 1。
	•	变量名 sum 不要使用，因为 sum 是 Python 内置函数，应换成 total 或 total_sum。
改正：
num = input('请输入一个正整数：')
try: 
    num = int(num)
    if num <= 0:
        print('请输入正整数')
    else:
        total = 0
        for i in range(1, num + 1):
            total += i  # 累加
        print(f'结果为 {total}')
except ValueError:
    print('你输入的不是正整数')
"""







"""
    3.使用 for 循环打印九九乘法表（9×9 乘法表），格式如下：
"""
i = 1
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{i} * {j} = {i*j}\t', end="")
    print()




"""
    4.程序随机生成一个 1~100 之间的整数，让用户猜测这个数字：
	•	如果用户输入的数字小于答案，提示“太小了！”
	•	如果用户输入的数字大于答案，提示“太大了！”
	•	如果用户猜对了，提示“恭喜你，猜对了！”，然后结束循环。
"""

a = input("输入你的猜测数：")
random_number = random.randint(1, 100) + 1
while True:
    a = int(a)
    if a == random_number:
        print('恭喜你，猜对了！')
        break
    elif a < random_number:
        print('太小了！')
        a = input("输入你的猜测数：")
    else:
        print('太大了！')
        a = input("输入你的猜测数：")
"""
    GPT老师的建议
    •	避免 ValueError，先判断 isdigit()，然后转换 int。
	•	防止输入无效数值（如负数、大于 100）。
	•	while True 放在输入判断内部，避免用户输入错误导致程序崩溃。

random_number = random.randint(1, 100) + 1  # 生成随机数
while True:
    a = input("输入你的猜测数：")  # 每次循环重新获取输入
    if not a.isdigit():  # 检查输入是否是整数
        print("请输入一个 1-100 之间的整数！")
        continue
    a = int(a)  # 转换成整数
    if a < 1 or a > 100:
        print("请输入 1 到 100 之间的数！")
    elif a < random_number:
        print("太小了！")
    elif a > random_number:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")
        break
"""




"""
    5.让用户输入一串字符（字符串），再输入一个字符 ch，然后用 for 循环统计这个字符在字符串中出现的次数。
"""
word = input('请输入字符串：')
your_char = input('请输入一个字符：')
count = 0
for char in word:
    if your_char == char:
        count += 1
print('{}在{}中出现了{}次'.format(your_char, word, count))






