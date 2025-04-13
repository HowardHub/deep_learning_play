
'''
不熟悉知识点：
1.幂函数：
    x ** y 等于用于计算 x 的 y 次方
    pow(x,y)
    math.pow(x,y) #适用于浮点数
    numpy.power(x,y) #适用于数组

2.嵌套的列表推导式
    [expression for item1 in iterable1 for item2 in iterable2 ... if condition]
    expression：最终生成的元素表达式。
    for item1 in iterable1：外层循环。
    for item2 in iterable2：内层循环（可以有多个）。
    if condition（可选）：过滤条件。

    生成二维列表： [[i*j for i in range(1,4)] for j in range(1,4)]
    展开二维列表：[num for row in matrix for num in row] #matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]，对matrix的循坏是外层循环。


'''


# 列表推倒式，专项训练
"""
1. 使用列表推导式创建一个包含数字 1 到 10 的列表，并打印它。
"""
# 示例输出: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = [i for i in range(1, 11)]
print(nums)

"""
2. 使用列表推导式生成一个包含 1 到 10 中每个数的平方的列表，并打印它。
"""
# 示例输出: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares = [i * i for i in nums]
print(squares)

"""
3. 使用列表推导式从一个列表 [3, 6, 9, 12, 15, 18, 21] 中筛选出能被 6 整除的数。
"""
# 示例输出: [6, 12, 18]
nums =  [3, 6, 9, 12, 15, 18, 21]
my_nums = [i for i in nums if i % 6 == 0]
print(my_nums)

"""
4. 使用列表推导式将字符串 "hello world" 中的每个字母转成大写字母，并组成一个新列表。
"""
# 示例输出: ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
new_str_list = [mychar.upper() for mychar in "hello world"]
print(new_str_list)

"""
5. 使用列表推导式过滤掉一个字符串列表中长度小于 5 的单词。
words = ["apple", "dog", "banana", "cat", "elephant"]
"""
# 示例输出: ['apple', 'banana', 'elephant']
words = ["apple", "dog", "banana", "cat", "elephant"]
words_less5 = [word for word in words if len(word) >= 5]
print(words_less5)


"""
6. 使用列表推导式生成一个列表，包含 1 到 20 中所有偶数对应的字符串，例如 "Even: 2"。
"""
# 示例输出: ['Even: 2', 'Even: 4', ..., 'Even: 20']
str_list = ['Even: {}'.format(num) for num in range(1, 21) if num % 2 == 0]
print(str_list)



"""
7. 使用列表推导式生成一个 2 的幂的列表，范围从 2^0 到 2^10。
"""
# 示例输出: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
pow_list = [2 ** x for x in range(0, 11)] #记得从0开始
print(pow_list)


"""
8. 使用嵌套列表推导式创建一个 3x3 的乘法表（二维列表）。
"""
# 示例输出: [[1,2,3], [2,4,6], [3,6,9]]
double_dim_list = [[i*j for i in range(1,4)] for j in range(1,4)]

print(double_dim_list)
print([num for row in double_dim_list for num in row]) #扩展，把二维数组展开成一维列表



"""
9. 给定两个列表 [1, 2, 3] 和 ['a', 'b', 'c']，使用列表推导式生成它们所有可能的组合对，例如 (1, 'a')。
"""
# 示例输出: [(1, 'a'), (1, 'b'), ..., (3, 'c')]
lista = [1,2,3]
listb = ['a', 'b', 'c']
combine_list = [(i,j) for i in lista for j in listb]
print(combine_list)




"""
10. 编写一个带有 if-else 条件表达式的列表推导式：对 1 到 10 中的每个数，如果是偶数就返回该数本身，否则返回字符串 "odd"。
"""
# 示例输出: ['odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd', 10]
mylist = [i if i%2 == 0 else 'odd' for i in range(1, 11) ]
print(mylist)







