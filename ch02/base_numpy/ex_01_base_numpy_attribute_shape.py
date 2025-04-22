import numpy as np


'''
关于numpy.shape的若干解释



在 NumPy 中，形状为 (n,) 的一维数组在与矩阵做点积运算时，会根据运算的顺序被自动视为行向量或列向量。
一维数组作为左操作数：当形状为 (n,) 的一维数组在左侧时，它被视为行向量 (1, n)
一维数组作为右操作数：当形状为 (n,) 的一维数组在右侧时，它被视为列向量 (n, 1)


并且如果点积运算的结果的为一维数组时，shape自动转为(n,)；即从(1,n)或(n,1)变为(n,)



'''

arr = np.array([1,2])
print(arr.shape)#(2,) 表示有 2 个元素的一维数组




#一维数组作为左操作数：当形状为 (n,) 的一维数组在左侧时，它被视为行向量 (1, n)
a = np.array([1,2])
x = np.array([[1,2,3], [3,4,2]])
dot_res = np.dot(a, x)
print(f'一维数组做左操作数时，结果的shape为{dot_res.shape}，结果为\n{dot_res}') #(1,2) (2,3) shape为(3,)


#一维数组作为右操作数：当形状为 (n,) 的一维数组在右侧时，它被视为列向量 (n, 1)
a = np.array([1,2])
x = np.array([[1,2],[2,3],[3,4]])
dot_res = np.dot(x, a)
print(f'一维数组做右操作数时，结果的shape为{dot_res.shape}，结果为\n{dot_res}') #(3,2) (2,1) shape为(3,)



