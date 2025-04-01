import numpy as np




"""
题目一：求数组元素之和
给定数组：
arr = np.array([1, 2, 3, 4, 5])
计算数组中所有元素的和。
"""
arr = np.array([1,2,3,4,5])
print(np.sum(arr))



"""
题目二：计算数组的平均值
给定数组：
arr = np.array([10, 20, 30, 40, 50])
计算数组的平均值。
"""
arr = np.array([10,20,30,40,50])
print(np.average(arr))



"""
题目三：找出数组的最大值和最小值
给定数组：
arr = np.array([5, 10, 15, 2, 7])
打印出数组中的最大值和最小值。
"""
arr = np.array([5, 10,15, 2, 7])
print(np.max(arr))
print(np.min(arr))


"""
题目四：找出数组最大值对应的索引
给定数组：
arr = np.array([3, 6, 9, 12, 15])
打印出数组中最大值对应的索引。
"""
arr = np.array([3,6,9,12,15])
print(np.argmax(arr))



"""
题目五：数组元素排序
给定数组：
arr = np.array([30, 10, 50, 20, 40])
对数组进行升序排序，并打印排序后的数组。
"""
arr = np.array([30,10,50,20,40])
print(np.sort(arr))


"""
题目六：数组拼接（concatenate）
给定两个数组：
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
使用np.concatenate()拼接成一个新数组。
"""
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.concatenate((a,b), axis=0))



"""
题目七：二维数组垂直堆叠（vstack）
给定两个数组：
a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])
使用np.vstack()垂直堆叠两个数组。
"""
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.vstack((a,b)))
#问题所在：
#题目给出的数组是二维的（形状为 (1,3)），但你实际创建的是一维数组（形状为 (3,)）。
#虽然vstack会自动处理一维数组，但建议严格按照题意明确二维数组，更好地展示你掌握了数组维度的知识。
a = np.array([[1, 2, 3]])  # 注意这里多一对[]
b = np.array([[4, 5, 6]])
print(f'修改后的vstack={np.vstack((a,b))}')



"""
题目八：二维数组水平堆叠（hstack）
给定数组：
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])
使用np.hstack()水平堆叠两个数组。
"""
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])
print(np.hstack((a,b)))


"""
题目九：数组拆分（split）
给定数组：
arr = np.array([10, 20, 30, 40, 50, 60])
使用np.split()将数组平均分成3份，并打印结果。
"""
arr = np.array([10, 20, 30, 40, 50, 60])
print(np.split(arr,3))


"""
题目十：数组方差与标准差
给定数组：
arr = np.array([4, 8, 12, 16, 20])
计算数组的方差和标准差。
"""
arr = np.array([4, 8, 12, 16, 20])
print(np.var(arr))
print(np.std(arr))