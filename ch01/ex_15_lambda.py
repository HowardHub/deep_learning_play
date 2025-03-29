
"""
基本语法：
    lambda arguments: expression
特点
    匿名性：没有函数名
    简洁性：通常只包含一个表达式
    一次性使用：适合简单操作，不适合复杂逻辑

sorted()介绍
    sorted(iterable, key=None, reverse=False)
    iterable：要排序的可迭代对象
    key：指定排序依据的函数（默认为 None，即直接比较元素）
    reverse：是否降序排序（默认为 False，即升序）

    
filter(), sorted(), map(), redeuce()这几个可以强化训练下。
"""

"""第9，10 题耗费多时"""



"""
📌 题目 1：简单的 Lambda 表达式
	•	使用 Lambda 表达式定义一个函数，计算一个数的平方。
	•	测试该函数，计算 5 的平方。
"""
f = lambda x: x*x
print(f(3))


"""
📌 题目 2：两个数相加
	•	使用 Lambda 表达式定义一个函数，接收两个参数并返回它们的和。
	•	测试函数，计算 3 和 7 的和。

"""
f = lambda a,b : a + b
print(f(3,7))


"""
📌 题目 3：Lambda 与 sorted() 配合
	•	给定列表：
    •	使用 sorted() 和 Lambda 表达式，根据分数从高到低排序。


"""
students = [
    {'name': '张三', 'score': 85},
    {'name': '李四', 'score': 92},
    {'name': '王五', 'score': 58},
    {'name': '赵六', 'score': 76}
]
"""
sorted() 函数会遍历 students 列表中的每个元素
对每个元素（这里每个元素是一个字典），调用 key 函数获取排序依据
lambda x: x['score'] 表示：
    接收一个参数 x（就是每个学生字典）
    返回 x['score']（即学生的成绩）
sorted() 根据这些成绩值进行排序
"""
res = sorted(students, key = lambda student:student['score'], reverse=True)
print(res)




"""
📌 题目 4：Lambda 表达式与 filter() 配合
    	•	使用 filter() 和 Lambda 表达式过滤出所有 偶数，并转为列表输出。
"""
numbers = [3, 7, 12, 20, 33, 41, 50]
nums = list(filter(lambda x : x % 2 == 0 ,numbers))
print(nums)







"""
📌 题目 5：Lambda 表达式与 map() 配合
	•	使用 map() 和 Lambda 表达式，去除每个字符串两端空格并转成全小写。
"""
fruits = [' apple ', 'banana', ' ORANGE ', 'Mango', 'waterMelon ']
fruits_new = list(map(lambda fruit: fruit.strip().lower()   ,fruits))
print(fruits_new)




"""
📌 题目 6：Lambda 表达式结合三元运算符
	•	使用 Lambda 表达式定义一个函数，判断一个整数是 "偶数" 还是 "奇数"。
	•	测试函数，输入数字 8 和 13。
    三元运算符：value_if_true if condition else value_if_false

"""
f = lambda x : '偶数' if x % 2 == 0 else '奇数'
print(f(8))
print(f(13))




"""
📌 题目 7：Lambda 实现字符串排序
	•	给定字符串列表：
    •	使用 Lambda 表达式按照 单词长度 进行排序（短的在前）。

"""
words = ['python', 'java', 'c', 'javascript', 'go']
res = sorted(words, key = lambda x : len(x))
print(res)




"""
📌 题目 8：Lambda 表达式与 reduce() 配合
	•	给定列表：
    •	使用 reduce() 和 Lambda 表达式计算列表中所有数字的 乘积。
	•	（提示：需要从 functools 中导入 reduce）
"""
from functools import reduce

numbers = [1, 2, 3, 4, 5]
res = reduce(lambda x,y : x * y, numbers)
print(res)




"""
📌 题目 9：Lambda 与列表解析
	•	使用 Lambda 表达式和列表解析创建一个函数，接收列表并返回该列表中所有元素的平方值列表。
	•	测试函数，输入 [2, 4, 6, 8]。
        预期输出：[4, 16, 36, 64]
    x for x in numbers
    lambda x : x
"""
numbers =  [2, 4, 6, 8]
# f = lambda x : (i*i for i in x) #返回一个生成器
f = lambda x :[i * i for i in x] #直接返回列表而不是生成器对象
print(f(numbers))


"""
📌 题目 10（综合挑战）：Lambda 结合字典排序
	•	给定字典：
    •	使用 Lambda 表达式将字典按值（分数）从高到低排序，并输出排序后的键值对列表。
"""
scores = {'张三': 85, '李四': 92, '王五': 58, '赵六': 76}
lst = list(sorted(scores.items(), key=lambda x:x[1], reverse=True))
print(lst)







