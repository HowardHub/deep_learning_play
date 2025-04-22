import numpy as np


'''
Numpy布尔索引专项训练


题目3
当你想对一个包含多个元素的数组进行布尔判断时，NumPy不知道你是想判断"任意一个元素为真"(any)还是"所有元素都为真"(all)。




'''


"""
题目1：选出大于5的元素
创建一个1维数组 `arr = np.array([1, 6, 3, 8, 2, 9])`，使用布尔索引选出大于5的元素。
"""
arr = np.array([1, 6, 3, 8, 2, 9])
mask = (arr > 5)
print(arr[mask])


"""
题目2：找出所有偶数
创建数组 `arr = np.arange(1, 11)`，使用布尔索引找出所有偶数。
"""
arr = np.arange(1, 11)
mask = arr % 2 == 0
print(arr[mask])

"""
题目3：选出满足两个条件的元素（大于3且小于8）
从 `arr = np.array([1, 4, 6, 8, 10])` 中选出大于3且小于8的元素。
"""
arr = np.array([1, 4, 6, 8, 10])
mask = (arr > 3) & (arr < 8)
#mask = (arr > 3) and (arr < 8) #错误写法。

print(arr[mask])


"""
题目4：布尔索引修改元素
将数组 `arr = np.array([3, 5, 7, 9, 11])` 中所有大于6的元素变成0。
"""
arr = np.array([3, 5, 7, 9, 11])
mask = arr > 6
arr[mask] = 0
print(arr)


"""
题目5：对二维数组进行布尔索引
给定二维数组 `arr = np.array([[1, 2], [3, 4], [5, 6]])`，找出所有大于3的元素。
"""
arr = np.array([[1, 2], [3, 4], [5, 6]])
mask = arr > 3
print(arr[mask])



"""
题目6：使用其他数组做条件
给定 `names = np.array(['Tom', 'Bob', 'Tom', 'Jerry'])` 和 `scores = np.array([80, 90, 85, 70])`，选出 Tom 的分数。
"""
names = np.array(['Tom', 'Bob', 'Tom', 'Jerry'])
scores = np.array([80, 90, 85, 70])
mask = names == 'Tom'
print(scores[mask])



"""
题目7：组合多个布尔条件
使用布尔索引选出 `arr = np.arange(1, 21)` 中既能被3整除又不能被4整除的数字。
"""
arr = np.arange(1, 21)
mask = (arr % 3 ==0) & (arr % 4 > 0)
print(arr[mask])


"""
题目8：使用布尔索引将不符合条件的元素替换为平均值
给定数组 `arr = np.array([10, 15, 20, 25, 30])`，将小于20的元素替换成数组的平均值。
"""
arr = np.array([10, 15, 20, 25, 30])
mean = np.mean(arr)
print(mean)
mask = arr < 20
arr[mask] = mean
print(arr)



"""
题目9：布尔索引结果与原数组保持形状一致（masked array风格）
对二维数组 `arr = np.array([[1, 2], [3, 4], [5, 6]])`，将小于4的元素替换为-1，其他保持不变。
"""
arr = np.array([[1, 2], [3, 4], [5, 6]])
mask = arr < 4
arr[mask] = -1
print(arr)



"""
题目10：根据多个布尔条件进行多维数组筛选
有以下数组：
arr = np.array([[5, 2, 3],
                [7, 8, 1],
                [6, 0, 9]])
请找出所有在第2列中小于5，且对应行第1列大于5的行。
提示：使用布尔数组作为行选择。
"""
arr = np.array([[5, 2, 3],
                [7, 8, 1],
                [6, 0, 9]])
#第1列大于5：arr[:, 0] > 5
#第2列小于5：arr[:, 1] < 5
mask = (arr[:, 0] > 5) & (arr[:, 1] < 5)
print(arr[mask])





######针对第10题二维条件筛选的强化练习。

"""
题目1：筛选第1列大于5的整行
给定数组：
arr = np.array([[4, 1],
                [6, 2],
                [7, 3],
                [3, 4]])
请找出第1列大于5的所有行。
"""
arr = np.array([[4, 1],
                [6, 2],
                [7, 3],
                [3, 4]])

mask = arr[:, 0] > 5
print(mask)
print(arr[mask])


"""
题目2：筛选第2列是偶数的所有行
给定数组：
arr = np.array([[1, 4],
                [2, 5],
                [3, 6],
                [4, 7]])
请找出第2列是偶数的行。
"""
arr = np.array([[1, 4],
                [2, 5],
                [3, 6],
                [4, 7]])

mask = arr[:, 1] % 2 == 0
print(arr[mask])


"""
题目3：筛选第1列小于3且第2列大于6的行
给定数组：
arr = np.array([[2, 7],
                [1, 9],
                [4, 5],
                [3, 8]])
请找出第1列小于3且第2列大于6的行。
"""
arr = np.array([[2, 7],
                [1, 9],
                [4, 5],
                [3, 8]])

mask = (arr[:, 0] < 3) & (arr[:, 1] > 6)
print(arr[mask])



"""
题目4：筛选第3列不等于0 且 第2列大于等于5 的行
给定数组：
arr = np.array([[1, 5, 0],
                [2, 6, 1],
                [3, 4, 2],
                [4, 5, 0]])
请找出第3列不等于0，且第2列大于等于5的行。
"""
arr = np.array([[1, 5, 0],
                [2, 6, 1],
                [3, 4, 2],
                [4, 5, 0]])
mask = (arr[:, 2] != 0) & (arr[:, 1] >= 5)
print(arr[mask])



"""
题目5：综合条件筛选
给定数组：
arr = np.array([[10, 3, 5],
                [8,  6, 2],
                [9,  2, 0],
                [7,  5, 1]])
请找出：
- 第1列大于8，或
- 第2列等于5，且第3列小于2  
的所有行。
"""
arr = np.array([[10, 3, 5],
                [8,  6, 2],
                [9,  2, 0],
                [7,  5, 1]])
mask = (arr[:, 0] > 8) | ((arr[:, 1] == 5) & (arr[:, 2] < 2))
print(arr[mask])


arr = np.array([[1, 5, 0],
                [2, -6, 1],
                [-3, 4, 2],
                [-4, 5, 0]])


mask = (arr <= 0)
print(mask)
arr[mask]  = 0
print(arr)






