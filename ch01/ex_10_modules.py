import math
import random
from math import pi
from random import randint

import math as m
import random as r

import my_module
import time
import os

import sys
import json

import datetime
import requests

"""
📌 题目 1：导入模块
	1.	导入 math 模块，并使用 math.sqrt() 计算 16 的平方根。
	2.	导入 random 模块，并生成一个 1 到 100 之间 的随机整数。
"""
print(math.sqrt(16))
print(random.randint(1,100))




"""
📌 题目 2：使用 from ... import
	1.	只从 math 模块导入 pi，然后打印 pi 的值。
	2.	只从 random 模块导入 randint，生成 10 到 20 之间的随机整数。
"""
print(pi)
print(randint(10,20))



"""
📌 题目 3：给模块起别名
	1.	用 import ... as 给 math 模块取别名 m，然后使用 m.pow(2, 3) 计算 2**3 并打印结果。
	2.	给 random 模块取别名 r，用 r.choice() 从 ['苹果', '香蕉', '橙子'] 中随机选一个水果。
"""
print(m.pow(2,3))
print(r.choice(['苹果', '香蕉', '橙子']))






"""
📌 题目 4：自定义模块
	1.	创建一个名为 my_module.py 的 Python 文件，其中定义一个函数 add(a, b)，返回 a + b 的结果。
	2.	在主程序中 导入 my_module，并调用 add(5, 10)，打印结果。
"""

# 保证termial在当前目录下，否则会报错
print(my_module.add(5,10))


"""
📌 题目 5：模块的 __name__
	1.	在 my_module.py 中添加：
	2.	直接运行 my_module.py，观察输出。 答：输入添加代码中的打印语句。
	3.	在主程序中 导入 my_module，再次运行，观察是否还有相同输出？  答：不会有任何输出。
"""





"""
📌 题目 6：探索 Python 标准库
	1.	使用 time 模块：
	•	获取当前时间戳（time.time()）。
	•	让程序暂停 2 秒，再打印 "休息 2 秒后执行"。
	2.	使用 os 模块：
	•	获取当前工作目录。
	•	列出当前目录下的所有文件。
"""
print(time.time())
#print(time.sleep(2))，返回的是一个None，所以不用打印
time.sleep(2)
print('休息 2 秒后执行')
print(os.getcwd()) #获取当前工作目录
print(os.listdir(os.getcwd())) #列出当前目录下的所有文件



"""
📌 题目 7：使用 sys 模块
	1.	打印 Python 解释器的版本信息。
	2.	打印所有导入的模块路径（sys.path）。
"""
print(sys.version)
print(sys.path)



"""
📌 题目 8：使用 json 模块
	1.	定义一个 Python 字典：
    2.	使用 json.dumps() 将字典转换为 JSON 格式的字符串，并打印结果。
	3.	使用 json.loads() 解析 JSON 字符串，转回 Python 字典。

"""
student = {"name": "张三", "age": 20, "city": "北京"}
json_str = json.dumps(student)
print(json_str)
student_dict = json.loads(json_str)
print(student_dict)




"""
📌 题目 9：使用 datetime 模块
	1.	获取并打印 当前日期和时间。
	2.	格式化时间 为 YYYY-MM-DD HH:MM:SS 格式，并打印。
"""
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))




"""
📌 题目 10：安装并使用第三方库
	1.	使用 pip 安装 requests 库：
    2.	使用 requests 发送 HTTP GET 请求，获取 https://api.github.com 的数据，并打印响应状态码。

"""
get_resp = requests.get('https://api.github.com')
print(get_resp.status_code)
print(get_resp.text)
