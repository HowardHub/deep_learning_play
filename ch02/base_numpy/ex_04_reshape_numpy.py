import numpy as np




"""
题目一：简单的reshape变换
创建一个包含6个元素的一维数组[1,2,3,4,5,6]，将其变成一个2行3列的数组。
"""
arr = np.array([1,2,3,4,5,6])
arr_new = arr.reshape(2,3)
print(arr_new)

"""
题目二：变换为一维数组（flatten）
给定数组：
arr = np.array([[1,2],[3,4],[5,6]])
将其变换为一维数组并打印。
"""
arr = np.array([[1,2],[3,4],[5,6]])
arr_flatten = arr.flatten()
print(arr_flatten)




"""
题目三：数组的转置（二维）
给定二维数组：
arr = np.array([[1, 2, 3], [4, 5, 6]])
对数组进行转置并打印。
"""
arr = np.array([[1,2,3], [4,5,6]])
arr_t = arr.T
print(arr_t)





"""
题目四：使用-1进行自动计算形状
创建一个包含8个元素的一维数组，从1到8，将它reshape为2行的数组，列数自动计算。
"""
arr = np.arange(1,9,1)
print(arr)
arr_reshape = arr.reshape(2, -1) #-1进行自动计算形状
print(arr_reshape)


"""
题目五：三维数组reshape为二维数组
给定三维数组：
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
将它reshape成一个2行4列的二维数组。
"""
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr_reshape = arr.reshape(2, 4)
print(arr_reshape)



"""
题目六：二维数组reshape为三维数组
给定二维数组：
arr = np.array([[1,2,3,4],[5,6,7,8]])
将其变换为三维数组，形状为(2,2,2)。
"""
arr = np.array([[1,2,3,4],[5,6,7,8]])
arr_reshape = arr.reshape(2,2,2)
print(arr_reshape)



"""
题目七：使用ravel展平数组
给定数组：
arr = np.array([[10,20,30],[40,50,60]])
使用ravel()方法将数组展平为一维数组。
"""
arr = np.array([[10,20,30],[40,50,60]])
arr_ravlel = arr.ravel()
print(arr_ravlel)



"""
题目八：数组的维度扩展
给定一维数组：
arr = np.array([1,2,3])
使用np.expand_dims()方法，在第0轴位置增加一个维度，打印数组及其shape。
"""
arr = np.array([1,2,3])
print(f'arr shape = {arr.shape}')
arr_expand_dims = np.expand_dims(arr, axis=0)
print(arr_expand_dims)
print(f'shape={arr_expand_dims.shape}')




"""
题目九：数组维度压缩
给定数组：
arr = np.array([[[1],[2],[3]]])
使用np.squeeze()方法压缩数组维度，并打印数组和shape。
"""
arr = np.array([[[1],[2],[3]]])
print(f'压缩前的shape={arr.shape}')
arr_sequeeze = np.squeeze(arr)
print(arr_sequeeze)
print(f'压缩后的shape={arr_sequeeze.shape}')





"""
题目十：数组转置（多维）
给定数组：
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
将数组的轴从(0,1,2)转置为(2,1,0)，并打印数组。
"""
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr.T)

"""
这里直接使用arr.T，它的默认行为是轴顺序倒置 (2,1,0)，此处虽然刚好与你题目要求的顺序相同，
但要清晰地掌握transpose方法，应明确写出：
"""

arr_transposed = arr.transpose(2,1,0)
print(arr_transposed)










