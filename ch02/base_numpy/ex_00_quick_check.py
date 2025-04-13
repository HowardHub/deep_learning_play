import numpy as np


"""



"""

# arr = np.array([1,2,3])
# print(arr[:])


A = np.array([[1,2], [3,4]])
B = np.array([[1,2], [3,4]])
print(A@B)
print('np.dot的结果取决于输入的形状。如果输入是向量，则是点积运算；如果是矩阵，则是矩阵乘法')
print(np.dot(A, B))
















# help(np.array)