import numpy as np

"""
	•数组(Array)创建
	•	np.array([1,2,3])
	•	np.zeros((2,3)) 创建全0数组
	•	np.ones((2,3)) 创建全1数组
	•	np.empty((2,3)) 创建空数组（未初始化）
	•	np.arange(start, stop, step) 创建连续数列
	•	np.linspace(start, stop, num) 创建等距数列
	•	np.eye(n) 单位矩阵
	•数组属性
	•	ndarray.shape 数组形状
	•	ndarray.size 数组元素数量
	•	ndarray.dtype 数据类型
	•	ndarray.ndim 数组的稚
"""

# print(np.array([1,2,3]))
# print(np.zeros((2,3)))
# print(np.ones((2,3)))
# print(f'创建空数组{np.empty((2,3))}')
# print(f'np.arange创建连续数列{np.arange(1,6,3)}')
# print(f'np.linsapce创建等距数列{np.linspace(1,6,3)}')
# print(f'创建单位矩阵{np.eye(5)}')



# a = np.eye(5)
# print(f'ndim：数组的秩（rank），即数组的维度数量或轴的数量{a.ndim}')
# print(f'shape：数组的形状，表示数组在每个轴上的大小。{a.shape}')
# print(f'size：数组中元素的总个数{a.size}')
# print(f'dtype：数组中元素的数据类型{a.dtype}')





"""
题目一：基本数组创建
创建一个数组，元素分别为[10, 20, 30, 40, 50]，并打印出数组及其dtype。
"""
arr = np.array([10, 20, 30, 40, 50])
print(arr)





"""
题目二：创建全零数组
创建一个3×4的全零数组（数据类型为float），并打印结果。
"""
arr = np.zeros((3,4), dtype=np.float32)
print(arr)


"""
题目三：创建全一数组R
创建一个长度为5的一维全一数组，并指定数据类型为int32。
"""
arr = np.ones(5, dtype=np.int32)
print(arr)
print(arr.dtype)





"""
题目四：创建空数组
创建一个大小为2×3的未初始化数组，并打印出数组。
注意：此数组中元素为随机值，输出可能每次都不同。
"""
arr = np.empty((2,3))
print(f'2x3的空数组:{arr}')





"""
题目五：创建连续整数数组（arange）
创建一个从5到15（不包含15），步长为2的整数数组。
"""
arr = np.arange(5, 15, 2)
print(arr)


"""
题目六：创建等距数组（linspace）
创建一个从0到1（含0和1）的含有5个元素的等间距数组。
"""
arr = np.linspace(0,1 ,5)
print(arr)


"""
题目七：创建单位矩阵
创建一个大小为4×4的单位矩阵。
"""
arr = np.eye(4, 4)
print(arr)





"""
题目八：随机数数组（均匀分布）
创建一个大小为2×5的随机数组，每个元素为0到1之间的随机浮点数。
注意：数组元素为随机生成，每次执行输出不同。
"""
arr = np.random.rand(2,5)
print(arr)



"""
题目九：随机整数数组
创建一个大小为3×3的随机整数数组，元素范围为10到20（包含10，不包含20）。
"""
arr = np.random.randint(10, 20, 9)
b = arr.reshape(3,3)
print(b)
# 更好的写法是直接指定数组形状，更清晰一些：
arr = np.random.randint(10, 20, size=(3, 3))
print(arr)



"""
题目十：模仿数组形状创建新数组
给定数组 a = np.array([[1, 2, 3], [4, 5, 6]])，创建一个与a相同形状的全零数组和全一数组。
"""
a = np.array([[1, 2, 3], [4, 5, 6]])
a1 = np.zeros(a.shape)
a2 = np.ones(a.shape)
print(a1)
print(a2)


