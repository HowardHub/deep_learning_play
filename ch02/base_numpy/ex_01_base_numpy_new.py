import numpy as np


"""
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
参数说明
object	数组或嵌套的数列。可以是任何类型
dtype	数组元素的数据类型，可选；有整形(int8,int16...)，浮点型(float16,float32...)，复数型(complex64,complex32,...)，布尔型(bool)，字符串型(str)
copy	对象是否需要复制，可选
order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
subok	默认返回一个与基类类型一致的数组
ndmin	指定生成数组的最小维度

"""
print('object的用法')
arr1 = np.array([1,2,3])
arr2 = np.array(['a','b', 'c'], dtype=str)
print(arr2.dtype)
mixarr = np.array([arr1, arr2], dtype=object)
print(mixarr.dtype)
arr = np.array([42, "NumPy", 3.14, [1, 2, 3], {"key": "value"}], dtype=object)
print(arr.dtype)


print('dtype的用法')
arr = np.array([1,2,3], dtype='float16')
arr = np.array([1,2,3], dtype=np.int32)
print(arr)

arr = np.array([False, True, False], dtype='bool')
arr = np.array([False, True, False], dtype=np.bool_)
arr = np.array([False, True, False], dtype=bool)
print(arr)

arr = np.array([1,2,3], dtype=np.complex64)
print(arr)


print('ndimn的用法')
arr = np.array([1,2,3], ndmin=2)
print(arr)



