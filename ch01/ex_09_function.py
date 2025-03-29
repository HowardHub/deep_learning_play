"""
📌 题目 1：定义一个简单的函数
	1.	定义一个函数 greet(name)，接收一个参数 name，返回 "Hello, xxx!" 。
	2.	调用 greet("张三") 并打印结果。
"""
def greet(name):
    return f'Hello, {name}!'
print(greet("张三"))




"""
📌 题目 2：计算两个数的和
	1.	定义一个函数 add(a, b)，返回 a 和 b 的和。
	2.	调用 add(5, 8) 并打印结果。
"""
def add(a, b):
    return a + b
print(add(5,8))





"""

📌 题目 3：计算列表的平均值
	1.	定义一个函数 average(lst)，接收一个包含数字的列表，返回它们的平均值。
	2.	测试 average([10, 20, 30, 40, 50]) 并打印结果。
"""
def average(lst):
    # sum = 0
    # for num in lst:
    #     sum += num
    return sum(lst) / len(lst)
print(f'列表的平均值{average([10, 20, 30, 40, 50])}')




"""
📌 题目 4：默认参数
	1.	定义一个函数 power(base, exp=2)，计算 base 的 exp 次幂（默认平方）。
	2.	调用 power(5) 和 power(2, 3)，并分别打印结果。
"""
def power(base, exp=2):
    # if exp is None:
    #     return pow(base, exp)
    # else:
    #     return pow(base, exp)
    # exp 默认值已经是 2，不会是 None，所以 if exp is None: 这部分不必要。
    return pow(base, exp)
print(power(5))
print(power(2,3))



"""
📌 题目 5：关键字参数
	1.	定义一个函数 student_info(name, age, city="北京")，返回学生的信息。
	2.	通过 位置参数 调用 student_info("李四", 18)。
	3.	通过 关键字参数 调用 student_info(age=20, name="王五", city="上海")。
"""
def student_info(name, age, city="北京"):
    return f'姓名：{name}, 年龄：{age}，城市：{city}'
print(student_info("李四", 18))
print(student_info(age=20, name="王五", city="上海"))





"""
**📌 题目 6：可变参数（*args 和 kwargs）
	1.	定义一个函数 sum_all(*args)，接收任意多个数，返回它们的和。
	2.	定义一个函数 print_info(**kwargs)，接收多个键值对，并逐行打印它们。
"""
def sum_all(*args):
    return sum(args)


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'key={key}, value={value}')


#错误调用：print(sum_all([2,2,3,4]))
print(sum_all(1,2,3))
#错误调用：print(print_info({'国家':'中国','姓名': '张三'}))
print_info(国家='中国', 姓名='张三', 年龄=30)




"""
📌 题目 7：递归函数
	1.	定义一个递归函数 factorial(n)，计算 n!（n 的阶乘）。
	2.	例如：factorial(5) -> 120。
"""
def factorial(n):
    if n == 1:
        return 1
    else: 
       return n * factorial(n-1)
print(factorial(5))






"""
📌 题目 8：Lambda 表达式
	1.	使用 lambda 定义一个匿名函数 square(x)，返回 x 的平方。
	2.	使用 lambda 计算两个数的和。
"""


square = lambda x : x * x
add = lambda x, y : x + y
print(square(2))
print(add(3,5))



"""
📌 题目 9：函数作用域
	1.	定义全局变量 x = 10。
	2.	定义一个函数 modify_x()，在函数内尝试修改 x = 20 并打印 x。
	3.	在函数外调用 modify_x() 后，再次打印 x，观察输出结果。
"""
x = 10
def modity_x():
    x = 20
    print(f'函数那修改x后，x={x}')
modity_x()
print(f'调用方法后，x={x}')


"""
注意：
如果想修改全局变量
x = 10
def modify_x():
    global x  # 声明使用全局变量
    x = 20
    print(f'函数内修改x后，x={x}')
modify_x()
print(f'调用方法后，x={x}')

"""




"""
📌 题目 10：函数作为参数
	1.	定义一个函数 apply_func(func, value)，它接收一个函数 func 和一个 value，返回 func(value) 的结果。
	2.	传入 lambda x: x * 3 和 10 进行测试。
"""
def apply_func(func, value):
    return func(value)

x = apply_func(lambda x: x * 3, 10)
print(x)