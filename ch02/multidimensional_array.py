import numpy as np


"""多维数组"""
x = np.array([1, 2, 3, 4])
print(x.ndim)
print(x.shape)




# 生成了一个3×2的数组B。3×2的数组表示第一个维度有3个元素，第二个维度有2个元素。
# 第一个维度对应第0维，第二个维度对应第1维
B = np.array([[1,2], [3,4], [5,6]])
print(B.ndim)
print(B.shape)





C = np.array([
        [[1,2], [3,4], [5,6]],
        [[1,2], [3,4], [5,6]],
        [[1,2], [3,4], [5,6]]
])
print('c')
print(C.ndim)
print(C.shape)




# 多维数组的乘法或点积运算
# 两个多维数组进行点积的前提：对应维度的元素个数必须相同
A = np.array([[1,2], [3,4], [5,6]]) # 3*2, 2*3
B = np.array([[1, 2, 3], [4,5,6]])
print(np.dot(A,B))
print(np.dot(B, A))


