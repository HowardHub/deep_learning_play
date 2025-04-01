import numpy as np







"""
题目一：数组类型创建
创建一个整数类型为int32的数组，数组元素为[1, 2, 3, 4, 5]，然后将它转换为float64类型并打印。
"""
arr = np.array([1,2,3,4,5], dtype=np.int32)
print(f'Original dtype: {arr.dtype}')
arr.astype(np.float64) #问题：调用了astype转换类型，但没有接收返回值，需要赋值给新数组（或原数组）才能完成类型转换
print(f'New dtype: {arr.dtype}')
print(arr)






"""
题目二：布尔数组转换
给定数组：arr = np.array([0, 2, 0, 5, 0])
请将其转换成布尔类型数组并打印结果。
"""
arr = np.array([0, 2, 0, 5, 0])
arr = arr.astype(np.bool_)
print(arr)



"""
题目三：字符串数组的创建
创建一个长度为4的字符串类型数组，内容为['apple', 'banana', 'cherry', 'date']，并打印其数据类型。
"""
arr = np.array(['apple', 'banana', 'cherry', 'date'])
print(f'dtype：{arr.dtype}')




"""
题目四：数据类型检测
给定数组：arr = np.array([1.5, 2.5, 3.5])
请编写代码检测该数组的数据类型是否为float64，如果是，则输出“数据类型为float64”，否则输出“不符合”。
"""
arr = np.array([1.5, 2.5, 3.5])
if arr.dtype == np.float64:
    print('数据类型为float64')
else:
    print('不符合')




"""
题目五：复数数组
创建一个复数类型的数组，数组元素分别为：[1+2j, 3+4j, 5+6j]，并打印出数组以及数组的dtype。
"""
arr = np.array([1+2j, 3+4j, 5+6j])
print(arr)
print(arr.dtype)









