'''
第8题不熟悉：列表推导式
第9题不熟悉:字符串的join方法
range(left, right)，含左不含右！

'''



"""
1. 创建一个列表 `fruits`，包含 "apple", "banana", "orange"，然后打印这个列表。
"""
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)


"""
2. 访问列表 `fruits` 中的第一个和最后一个元素，并打印它们。
"""
print(f'第一个元素{fruits[0]}')
print('最后一个元素%s' % (fruits[-1]))


"""
3. 往列表 `fruits` 末尾添加一个新元素 "grape"，再打印整个列表。
"""
fruits.append('grape')
print(fruits)

"""
4. 将列表 `fruits` 中的 "banana" 替换成 "watermelon"，然后打印更新后的列表。
"""
fruits[1] = 'watermelon'
print(fruits)


"""
5. 删除列表 `fruits` 中的第一个元素，并打印剩下的列表。
"""
del fruits[0]
print(fruits)

"""
6. 使用 for 循环遍历列表 `fruits`，并打印每一个元素。
"""
for fruit in fruits:
    print(fruit)

"""
7. 创建一个包含 1 到 10 的整数列表 `nums`，然后打印前5个元素（使用切片）。
"""
nums = list(range(1, 11)) #含左不含右，所以是range(1,11)
print(nums[:5])


"""
8. 将列表 `nums` 中的所有偶数筛选出来，并创建一个新列表 `evens`，然后打印它。
"""
evens = [x for x in nums if x % 2 ==0] #列表推导式
print(evens)

"""
9. 将列表 `fruits` 中所有元素用逗号连接成一个字符串，然后打印这个字符串。
"""
f_str = ','.join(fruits)
print(f_str)
"""
10. 使用列表推导式，生成一个包含 1 到 20 中所有平方数的列表 `squares`，然后打印它。
"""
squares = [x * x for x in range(1, 21)]
print(squares)


'''
现在请针对“列表推导式”这个知识点，从易到难，给我出10道题。
你出完题目后，再把这10个题目弄成一个可以复制的整体，并且每个题目都用python文档注释"""单独包起来，
这样做的目的是方便我一次性把所有题目录入到vscode中。
'''