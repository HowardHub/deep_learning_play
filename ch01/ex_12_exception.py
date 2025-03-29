import math

import logging

# 这里面的10道题目，只有第5题，GPT老师认为是完全对的，其他的都有问题。
# 建议查看书籍里面关于异常的描述。



"""
📌 题目 1：捕获异常
	1.	编写一个函数 divide(a, b)，返回 a / b 的结果。
	2.	如果 b == 0，捕获 ZeroDivisionError，并返回 "除数不能为 0"。
"""
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('除数不能为 0')
    return a / b

try:
    print(divide(1,0))
except ZeroDivisionError as e:
    print(e)

"""
问题：
    你在 divide 函数中手动抛出了 ZeroDivisionError，
    但 ZeroDivisionError 本来就是 Python 内置的，a / b 时会自动触发，不需要手动 raise。
改进：
    直接 try-except 捕获异常即可：
"""
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return '除数不能为0'





"""
📌 题目 2：处理多个异常
	1.	编写一个函数 convert_to_int(s)，尝试将字符串 s 转换为整数并返回。
	2.	如果 s 不能转换为整数，捕获 ValueError 并返回 "无法转换为整数"。
	3.	如果 s 是 None，捕获 TypeError 并返回 "输入不能为 None"。
"""
def convert_to_int(s):
    if s == None:
        raise TypeError( '输入不能为 None')
    try:
        return int(s)
    except ValueError as e:
        return '无法转换为整数'
    
print(convert_to_int('23'))
convert_to_int(None)
convert_to_int('a')

"""
	1.	if s == None: 应该用 if s is None:（Python 规范）
	2.	你在 s is None 时直接 raise TypeError，但后面 except 并没有捕获它，这样程序会崩溃。

"""
def convert_to_int(s):
    try:
        if s is None:
            raise TypeError('输入不能为None')
        return int(s)
    except ValueError:
        return '无法转换为整数'
    except TypeError:
        return '输入不能是None'






"""
📌 题目 3：使用 finally 语句
	1.	编写一个函数 read_file(filename)，尝试打开 filename 并读取内容。
	2.	如果文件不存在，捕获 FileNotFoundError 并返回 "文件未找到"。
	3.	使用 finally 确保无论是否出现异常，都打印 "文件操作结束"。
"""

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileExistsError:
        return '文件未找到'
    finally:
        print('文件操作结束')

"""
	问题：FileExistsError 不适用于 “文件未找到” 的情况。正确的异常应该是 FileNotFoundError。
"""
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return '文件未找到'
    finally:
        print('文件操作结束')






"""
📌 题目 4：try-except-else 结构
	1.	编写一个函数 sqrt_number(n)，返回 n 的平方根（使用 math.sqrt(n)）。
	2.	如果 n 是负数，捕获 ValueError 并返回 "不能计算负数的平方根"。
	3.	如果没有异常，打印 "计算成功"，并返回结果。
"""
def sqrt_number(n):
    try:
        return math.sqrt(n)
    except ValueError as e:
        print('不能计算负数的平方根')

"""
问题：math.sqrt(n) 对负数会抛出 ValueError，但你的 except 里只是 print() 了错误信息，
     并没有返回任何值，会导致 None 返回。

"""
def sqrt_number(n):
    try:
        res = math.sqrt(n)
    except ValueError:
        return '不能计算负数的平方根'
    else:
        print('计算成功')
        return res





"""
📌 题目 5：自定义异常
	1.	定义一个自定义异常 NegativeNumberError，继承 Exception。
	2.	编写一个函数 check_positive(n)：
	•	如果 n < 0，抛出 NegativeNumberError。
	•	如果 n >= 0，返回 "输入正确"。
"""
class NegativeNumberError(Exception):
    pass


def check_positive(n):
    if n < 0:
        raise NegativeNumberError('')
    else:
        return '输入正确'








"""
📌 题目 6：嵌套 try-except
	1.	编写一个函数 nested_try(a, b, c)：
	•	第一层 try：计算 a / b。
	•	第二层 try（嵌套）：将结果转换为整数并计算 c 的平方。
	•	处理 ZeroDivisionError、ValueError 并返回相应的错误信息。
"""
def nested_try(a, b, c):
    try:
        res = a / b
        try:
            res = int(res) + c * c
        except ValueError as e:
            e.print()
    except ZeroDivisionError as e:
        e.print()

"""
问题：
	1.	e.print() 语法错误，Exception 对象没有 print() 方法，应该使用 print(e)。
	2.	except ValueError 里并不会报错，因为 int(res) 转换失败也不会触发 ValueError（它会转换成 0 或 1）。
	3.	int(res) + c * c 不会引发 ValueError，但 c 可能是字符串等类型，这时 TypeError 更合适。
"""
def nested_try(a, b, c):
    try:
        res = a / b
        try:
            return int(res) + c * c
        except TypeError as e:
            print('数据类型错误', e)
    except ZeroDivisionError as e:
        print('除零错误', e)





"""
📌 题目 7：使用 raise 关键字
	1.	编写一个函数 check_age(age)：
	•	如果 age < 18，使用 raise ValueError("未成年人禁止注册") 抛出异常。
	•	否则，返回 "注册成功"。
"""
def check_age(age):
    if age < 18:
        raise ValueError('未成年人禁止注册')
    else:
        return '注册成功'

"""
	•	else 语句其实可以去掉，直接 return。
"""






"""
📌 题目 8：日志记录异常
	1.	导入 logging 模块，配置日志级别为 ERROR。
	2.	编写 log_exception() 函数，尝试除以 0 并捕获 ZeroDivisionError。
	3.	发生异常时，使用 logging.error() 记录错误信息。
"""
def log_exception():
    try:
        a = 10/0
    except ZeroDivisionError as e:
        logging.error(e)
"""
	•	logging 没有配置，会导致日志看不到。
"""
def log_exception():
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
    try:
        a = 10 / 0
    except ZeroDivisionError as e:
        logging.error("除零错误: %s", e)






"""
📌 题目 9：使用 assert 进行调试
	1.	编写 check_even(n)：
	•	使用 assert n % 2 == 0, "输入的不是偶数" 确保 n 为偶数。
	•	如果 n 是偶数，返回 "是偶数"。
	•	如果 n 不是偶数，触发 AssertionError 并返回错误信息。
"""
def check_even(n):
    assert n % 2 == 0, '输入的不是偶数'

"""
	•	assert 抛出的 AssertionError 并不会被捕获，代码执行失败时不会返回任何内容。
"""
def check_even(n):
    try:
        assert n % 2 == 0, '输入的不是偶数'
        return '是偶数'
    except AssertionError as e:
        return str(e)






"""
📌 题目 10：异常处理综合应用
	1.	编写 process_data(data)：
	•	data 应该是一个 字典，包含键 name 和 age。
	•	读取 data["name"] 和 data["age"] 并返回 "姓名: xx, 年龄: xx"。
	•	处理 KeyError（如果键不存在）、TypeError（如果 data 不是字典）。
"""
def  process_data(data):
    if not isinstance(data, dict):
        raise TypeError('不是字典类型的数据')
    if 'name' not in data or 'age' not in data: # 直接抛出异常可能导致调用者需要额外处理，可以利用 Python 的内置 KeyError 机制，减少手动检查
        raise KeyError('键不存在')
    return f'姓名：{data['name']}，年龄：{data['age']}'

"""
问题：
	1.	raise KeyError('不是字典类型的数据') 应该是 raise TypeError('不是字典类型的数据')，因为数据类型错误不属于 KeyError。
	2.	return f'姓名：{data['name']}，年龄：{data['age']}' 会报错，因为 f'' 里用了 ""。
"""
def process_data(data):
    try:
        if not isinstance(data, dict):
            raise TypeError('不是字典类型的数据')
        return f"姓名：{data['name']}，年龄：{data['age']}"
    except KeyError:
        return '键不存在'
    except TypeError as e:
        return str(e)


"""grok的简洁版本"""
def process_data(data):
    if not isinstance(data, dict):
        return '不是字典类型的数据'
    try:
        return f"姓名：{data['name']}，年龄：{data['age']}"
    except KeyError:
        return '键不存在'




