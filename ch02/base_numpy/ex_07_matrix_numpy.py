import numpy as np

'''
矩阵乘法是“行与列的线性组合”，向量点积是“对应元素相乘后求和”。矩阵乘积
AB 的第 (i,j)元素，实际上是A 的第 i 行向量与 B 的第 j 列向量的点积。

在Python的NumPy中，np.dot(a, b) 的行为取决于输入形状
	若 a 和 b 是向量，计算点积；
    若 a 和 b 是矩阵，计算矩阵乘法（等价于 a @ b）
    
在深度学习框架（如PyTorch）中，torch.dot 严格用于向量点积，而矩阵乘法用 @ 或 torch.matmul


'''

"""
题目一：矩阵乘法（二维数组）
给定两个二维数组（矩阵）：
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
计算矩阵A与B的矩阵乘法，并打印结果。
"""
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])
print( A * B)

"""
	•	问题：
            A * B 执行的是逐元素相乘（element-wise multiplication），而不是矩阵乘法。
	•	正确的矩阵乘法应使用：
	•	np.dot(A, B)
	•	或者 A @ B (推荐使用此方式，更简洁明了)
"""
print(A@B)



"""
题目二：矩阵的点积（dot函数）
给定数组：
a = np.array([1,2,3])
b = np.array([4,5,6])
计算两个向量的点积（内积）。
"""
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a.dot(b))



"""
题目三：矩阵转置
给定矩阵：
arr = np.array([[1,2,3],[4,5,6]])
对矩阵进行转置，并打印结果。
"""
arr = np.array([[1,2,3], [4,5,6]])
print(arr.T)


"""
题目四：单位矩阵创建
创建一个大小为3×3的单位矩阵，并打印结果。
"""
print(np.eye(3,3))




"""
题目五：计算矩阵行列式
给定矩阵：
arr = np.array([[1,2],[3,4]])
计算矩阵的行列式（determinant）。
"""
arr = np.array([[1,2], [3,4]])
print(np.linalg.det(arr))


"""
题目六：矩阵求逆
给定矩阵：
arr = np.array([[4,7],[2,6]])
求出矩阵的逆矩阵。
"""
arr = np.array([[4,7], [2,6]])
print(np.linalg.inv(arr))



"""
题目七：矩阵特征值与特征向量
给定矩阵：
arr = np.array([[1,2],[3,4]])
计算矩阵的特征值和特征向量，并打印结果。
"""
arr = np.array([[1,2], [3,4]])
eigenvalues, eigenvectors = np.linalg.eig(arr)
print("特征值:", eigenvalues)
print("特征向量:\n", eigenvectors)


"""
题目八：解线性方程组
给定线性方程组：
2x + 3y = 8
x + 2y = 5
用NumPy计算方程组的解，并打印。
"""
A = np.array([[2,3], [1,2]])
b = np.array([8,5])
x = np.linalg.solve(A,b)
print(x)


"""
题目九：矩阵的秩
给定矩阵：
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
计算矩阵的秩(rank)。
"""
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
rank = np.linalg.matrix_rank(arr)
print(rank)

"""
题目十：矩阵的迹（trace）
给定矩阵：
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
计算矩阵的迹（主对角线元素的和）。
"""
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.trace(arr))


#NumPy 会自动根据运算需求，将 1D 向量视为行或列向量
#在 NumPy 中，A = np.array([1, 2]) 是一个 1D 向量，它没有明确的“行向量”或“列向量”身份。NumPy 会根据上下文自动处理它的维度
A = np.array([1,2])
B = np.array([[1,2], [3,4]])
C = np.dot(A,B)
D = np.dot(B,A)
print(f'AB={C}，此时 NumPy 自动将 A 视为行向量 (1×2)，与 B 相乘得到 1×2 向量')
print(f'BA={D}，此时 NumPy 自动将 A 视为列向量 (2×1)，与 B 相乘得到 2×1 向量')








