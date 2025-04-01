import numpy as np



"""
题目一：数组与标量运算（加法）
创建数组arr = np.array([1,2,3,4])，对数组每个元素加上数字10。
"""
arr = np.array([1,2,3,4])
b = arr + 10
print(b)




"""
题目二：数组与数组的简单运算
创建数组：
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
计算并打印数组a与b的逐元素相乘结果。
"""
a = np.array([1,2,3])
b = np.array([10,20,30])
c = a * b
print(c)



"""
题目三：数组与标量的除法运算
创建二维数组：
arr = np.array([[10, 20], [30, 40]])
将数组的每个元素除以10，并打印结果。
"""
arr = np.array([[10, 20], [30, 40]])
print(arr / 10)



"""
题目四：数组广播（一维对二维）
给定数组：
arr = np.array([[1,2,3], [4,5,6]])
b = np.array([10,20,30])
使用广播机制，将arr和b相加。
"""
arr = np.array([[1,2,3], [4,5,6]])
b = np.array([10,20,30])
print(arr + b)


"""
题目五：广播与列运算
给定二维数组：
arr = np.array([[1,2,3],[4,5,6]])
b = np.array([[10],[20]])
计算arr+b并打印结果。
"""
arr = np.array([[1,2,3], [4,5,6]])
b = np.array([[10], [20]])
print(arr + b)




"""
题目六：广播实现数组中心化
给定数组：
arr = np.array([[1, 2], [3, 4], [5, 6]])
计算每列的平均值，然后用广播机制将数组的每一列减去对应列的平均值。
"""
arr = np.array([[1,2], [3,4], [5,6]])
avg = np.mean(arr, axis=0)
print(avg)
print(arr /avg)
# 题目要求的是数组中心化，应是每列元素减去列的平均值，而不是除以平均值。
print(arr - avg)  # 改成减法即可




"""
题目七：广播实现行标准化
给定数组：
arr = np.array([[1, 2, 3], [4, 5, 6]])
用广播机制实现每行元素除以所在行的和（行标准化）。
"""
arr = np.array([[1,2,3], [4,5,6]])
cols_sum = np.sum(arr, axis=1)
print(arr / cols_sum.reshape(2,1))





"""
题目八：多维广播运算
给定数组：
arr = np.array([[[1],[2],[3]],[[4],[5],[6]]])
b = np.array([10,20,30])
计算arr+b，打印结果。
"""
arr = np.array([[[1],[2],[3]],[[4],[5],[6]]])
print(arr.shape) #(2, 3, 1)
b = np.array([10,20,30])
print(b.shape) #(3,)
res = arr + b
print(res.shape) #(2, 3, 3)
print(res)


"""
题目九：广播机制（维度不匹配的情况）
解释下面两个数组：
a = np.array([[1],[2],[3]])
b = np.array([10,20])
尝试计算a+b，然后打印结果，并思考为什么会成功。
"""
a = np.array([[1], [2], [3]])
print(a.shape) #3*1
b = np.array([10,20])
print(b.shape) #2
print(a + b) #a+b，最大行为3，最大列为2，所以数组a被广播成3*2，数组b也被广播成3*2





"""
题目十：广播机制应用（计算距离）
给定二维数组中的坐标点points：
points = np.array([[1,1],[2,2],[3,3]])
origin = np.array([0,0])
使用广播机制，计算每个点到origin点的欧氏距离（Euclidean distance），并打印。
"""
points = np.array([[1,1], [2,2], [3,3]])
origin = np.array([0, 0])
distance = np.linalg.norm(points - origin)
print(distance)

#你直接用np.linalg.norm()计算二维数组到点的距离时，没有指定轴，会返回一个单一的值（整体范数），而不是各个点到原点的距离。
distance = np.linalg.norm(points - origin, axis=1)  # 应指定axis=1
print(distance)





