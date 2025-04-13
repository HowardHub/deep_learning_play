

'''
三目表达式专项训练
1.三目表达式：
    value_if_true if condition else value_if_false
    i if i % 2 == 0 else 'odd'

Python 中空列表 [] 在布尔上下文中被视为 False，非空列表被视为 True，因此可以直接用 if not list 判断：
    my_list = []
    if not my_list:
        print("列表为空")  # 输出: 列表为空
    else:
        print("列表非空")

判断字符串为空也可以直接写成
    if not s:
        print('字符串为空')
    else:
        print('字符串不为空')
'''


'''
现在请针对“三目表达式”这个知识点，从易到难，给我出10道题。
你出完题目后，再把这10个题目弄成一个可以复制的整体，并且每个题目都用python文档注释"""单独包起来，
这样做的目的是方便我一次性把所有题目录入到vscode中。
'''



"""
1. 判断一个整数 num 是否为正数，是则返回 "positive"，否则返回 "non-positive"。
"""
# 示例输出: positive 或 non-positive
def is_positive(num):
    return 'positive' if num > 0 else 'non-positive'
print(is_positive(10))
print(is_positive(-1))

"""
2. 判断一个字符串 s 是否为空，是则返回 "Empty"，否则返回 "Not Empty"。
"""
# 示例输出: Empty 或 Not Empty
def is_empty(s):
    return 'Empty' if s is None or s == '' else 'Not Empty'
print(is_empty('bac'))
print(is_empty(''))


"""
3. 判断一个年龄变量 age 是否大于等于18，是则返回 "Adult"，否则返回 "Minor"。
"""
# 示例输出: Adult 或 Minor
def is_adult(age):
    return 'Adult' if age >= 18 else 'Minor'
print(is_adult(19))
print(is_adult(9))


"""
4. 比较两个变量 a 和 b，返回较大的一个。
"""
# 示例输出: 20 （如果 a=10, b=20）
a = 10
b = 20
c = a if a >= b else b
print(c)




"""
5. 判断一个年份 year 是否是闰年，是则返回 "Leap Year"，否则返回 "Not Leap Year"。
（闰年规则：能被4整除且不能被100整除，或者能被400整除）
"""
# 示例输出: Leap Year 或 Not Leap Year
def is_leap_year(year):
    return 'Leap Year' if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)   else 'Not Leap Year'

print(is_leap_year(2018))
print(is_leap_year(2020))


"""
6. 给定一个成绩 score，使用三目表达式判断成绩是否及格（>=60），返回 "Pass" 或 "Fail"。
"""
# 示例输出: Pass 或 Fail
def is_pass(score):
    return 'Pass' if score >= 60 else 'Fail'
print(is_pass(70))
print(is_pass(30))


"""
7. 使用三目表达式返回列表 lst 的第一个元素，如果列表为空则返回 "Empty list"。
"""
# 示例输出: 第一个元素或 Empty list
def get_first(lst):
    return lst[0] if lst else 'Empty list'

print(get_first(['a','b']))
print(get_first([]))

"""
8. 使用三目表达式返回一个数字是否为偶数，是则返回该数字的平方，否则返回它本身。
"""
# 示例输出: 16 （如果 num = 4），或 5（如果 num = 5）
def is_even(num):
    return num * num if num % 2 == 0 else num
print(is_even(4))
print(is_even(5))


"""
9. 写一个三目表达式，根据变量 temp 的值判断天气描述：
   - 大于30: "Hot"
   - 介于20-30: "Warm"
   - 否则: "Cold"
   （提示：可以嵌套使用三目表达式）
"""
# 示例输出: Hot, Warm, Cold
def get_temp(temp):
    return  'Hot' if temp > 30 else ('Warm' if temp>=20 and temp <= 30 else 'Cold')
print(get_temp(10))
print(get_temp(25))
print(get_temp(38))

"""
10. 使用列表推导式与三目表达式结合，对一个整数列表 nums 中的每个数：
    - 如果是偶数则返回它除以2
    - 如果是奇数则返回它乘以3
    生成新列表并打印。
"""
# 示例输入: [1, 2, 3, 4]
# 示例输出: [3, 1, 9, 2]
inpt =  [1, 2, 3, 4]
outpt = [i//2 if i%2 == 0 else i * 3 for i in inpt] #除法 / 默认返回浮点数，如果你希望返回整数，可以用 // 代替。
print(outpt)



