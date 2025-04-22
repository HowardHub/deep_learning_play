import numpy as np


"""
enumerate的用法
是一个内置函数，用于在遍历可迭代对象（如列表、元组、字符串等）时，同时获取元素的索引和值。
它返回一个枚举对象，生成由索引和对应值组成的元组。

enumerate(iterable, start=0)
    iterable：要枚举的可迭代对象（如列表、字符串等）。
    start（可选）：索引的起始值，默认为 0。




"""
print('enumerate演示：迭代列表')
fruits = ['apples', 'bananas', 'oranges']
for index, val in enumerate(fruits): #没有enumerate的写法  for i in range(len(fruits)):
    print(index, ':', val)




print('enumerate演示：迭代元组')
fruits = ('apples', 'bananas', 'oranges')
for index, val in enumerate(fruits):
    print(index, ':', val)


print('enumerate演示：迭代字典')
my_dict = {'name':'章三', 'age':18, 'score': 199}
for index, (key, val) in enumerate(my_dict.items()):
    print(index,',',key,':', val)


print('enumate遍历字符串')
mystr = 'people'
for i,chr in enumerate(mystr):
    print(i,':', chr)




print('enumerate迭代矩阵')
'''
结果
0 : [1 2 3]
1 : [4 5 6]
'''
X = np.array([[1,2,3], [4,5,6]])
for idx, val in enumerate(X):
    print(idx,':', val)




