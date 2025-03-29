
"""
装饰器
    它允许你在不修改原函数代码的情况下，为函数添加额外的功能。
    装饰器本质上是一个高阶函数，它接受一个函数作为参数，并返回一个新的函数。
    装饰器的核心思想是"函数是一等公民"，即函数可以作为参数传递，也可以作为返回值。
基本语法：
@decorator
def function():
    pass
    
等价于
def function():
    pass
function = decorator(function)



所有装饰器的 wrapper 函数：最好都用 @functools.wraps(func) 来保留原函数信息（如题目8一样）。
"""




"""
📌 题目 1：最简单的装饰器

定义一个简单的装饰器 say_hello，在函数调用前打印 "Hello!"。
"""
def say_hello(func): #函数作为装饰器的参数
    def wrapper(): #这里千万不能写成wrapper(func)
        print('Hello!')
        func()
    return wrapper #返回装饰后的函数

@say_hello
def tiktok():
    print('tiktok')

tiktok()



"""
📌 题目 2：装饰器修改函数返回值
定义装饰器 square_result，让被装饰函数的返回值始终是原来结果的平方。
"""
def square_result(func):
    def wrapper(*args, **kwargs): #使用*args和**kwargs接收任意参数：
        return  func(*args, **kwargs) * func(*args, **kwargs) #传递参数给原函数
    return wrapper

# 测试用例：
@square_result
def add(x, y):
    return x + y

print(add(2, 3))
"""
   优化：将return  func(*args, **kwargs) * func(*args, **kwargs)
   改为： 
   result = func(*args, **kwargs)
   return result * result

"""




"""
📌 题目 3：带参数的装饰器（定制前缀）
定义一个带参数的装饰器 prefix(text)，它会在调用函数前打印指定的前缀文本。
"""
def prefix(text):
    def decorate_prefix(func):
        def wrapper():
            print(text)
            func()
        return wrapper
    return decorate_prefix

# 测试用例：
@prefix("【提示】")
def info():
    print("这里是重要信息！")

info()




"""
📌 题目 4：计算函数运行时间

定义装饰器 measure_time，用于计算并打印函数的执行时间（秒）。
	•	提示：可使用time.time()。
"""
import time

def measure_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('函数运行了 {:.2f} 秒'.format(end - start))
    return wrapper


# 测试用例：
@measure_time
def slow_func():
    time.sleep(2)

slow_func()




"""
📌 题目 5：多个装饰器叠加

定义两个简单装饰器 bold 和 italic：
	•	bold 将函数返回的字符串加上 <b> ... </b> 标签。
	•	italic 将函数返回的字符串加上 <i> ... </i> 标签。
"""


def bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def italic(func):
    def wrapper():
        return '<i>' + func() + '</i>'
    return wrapper


# 测试用例：
@bold
@italic
def greeting():
    return "Hello!"

print(greeting())



"""
📌 题目 6：装饰器记录函数调用次数

    定义装饰器 count_calls，记录函数被调用的次数，每次调用时打印调用次数。

"""
def count_calls(func):
    def wrapper():
        print(f'第 {1} 次调用函数')
        func()
    return wrapper

def count_calls(func):
    def wrapper():
        wrapper.calls += 1
        print(f'第 {wrapper.calls} 次调用函数')
        func()
    wrapper.calls = 0
    return wrapper

# 测试用例：
@count_calls
def hello():
    print("Hello!")

hello()
hello()
hello()


"""
	•	没有实际计数功能，每次调用都是打印第 1 次。
    使用函数属性记录调用次数
"""






"""
📌 题目 7：类装饰器

定义一个类装饰器 AddGreeting：
	•	用于装饰函数，调用函数前先打印 “Welcome!”，调用后打印 “Goodbye!”。


"""
class AddGreeting:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('Welcome!')
        self.func()
        print('Goodbye!')

# 测试用例：
@AddGreeting
def say():
    print("Python")

say()




"""
📌 题目 8：使用 functools.wraps
    定义装饰器 log_func，使用 functools.wraps 保持被装饰函数的元信息（如函数名、文档字符串等）。
"""


import functools

def log_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #func() # # 这里应该return，否则装饰后的函数返回None
        return func(*args, **kwargs)
    return wrapper

# 测试用例：
@log_func
def my_function():
    """这是函数的文档字符串"""
    print("执行函数")

print(my_function.__name__)
print(my_function.__doc__)




"""
📌 题目 9：装饰器处理异常
定义装饰器 safe_divide，捕获并处理被装饰函数中的 ZeroDivisionError 异常，如果发生异常，打印 "错误：除数不能为0"。

"""

def safe_divide(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print('错误：除数不能为0')
    return wrapper


# 测试用例：
@safe_divide
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(5, 0))





"""
📌 题目 10：装饰类方法
定义一个装饰器 check_positive，装饰类方法，用于检查方法参数是否为正数，若为负数或零，则打印错误信息并不执行方法。
"""


# def check_positive(func):
#     def wrapper(*args, **kwargs):
#         if args[0] <= 0:
#             print('参数不能是负数')
#         else:
#             return func(*args, **kwargs)
#     return wrapper


def check_positive(func):
    def wrapper(self, x, *args, **kwargs):
        if x <= 0:
            print('错误：参数不能是负数')
        else:
            return func(self, x, *args, **kwargs)
    return wrapper

# 测试用例：
class Calculator:
    @check_positive
    def sqrt(self, x):
        print(f"计算{x}的平方根")

calc = Calculator()
calc.sqrt(9)
calc.sqrt(-4)


"""
存在问题：
	•	类方法的第一个参数为self，实际需要检查的是args[1]而非args[0]。
	•	提示文本与题目不完全一致，应改为：“错误：参数必须为正数”。
"""





