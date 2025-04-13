import numpy as np


"""


numpy.sum(arr, axis=None, dtype=None, keepdims=False, initial=0)

arr
    输入数组（可以是 NumPy 数组或类似数组的对象）。
axis（可选）
    指定求和的轴（方向）。默认为 None，表示对所有元素求和。
    如果是一个整数（如 axis=0 或 axis=1），则沿指定轴求和。
    如果是元组（如 axis=(0, 1)），则对多个轴求和。
dtype（可选）
    指定返回结果的数据类型。例如 dtype=np.float32。默认情况下，会根据输入数组的类型自动推断。
keepdims（可选）
    如果为 True，保持求和后的维度与原数组一致（结果为 1 的维度）。
    默认为 False，会去掉求和后的维度。
initial（可选）
    求和的初始值（默认为 0）。

    
返回一个标量或数组（取决于 axis 的设定），包含求和结果。



空数组求和：如果输入数组为空（如 np.array([])），默认返回 0（可通过 initial 修改）。
布尔数组：布尔类型会被隐式转换为整数（True=1, False=0），求和结果为整数。



"""
# help(np.sum)

print('对所有元素求和')
a = np.array([1,2,3])
print(np.sum(a))

print('沿指定轴求和')
b = np.array([[1,2,3], [4,5,6]])
print(np.sum(b, axis=1))
print(np.sum(b, axis=0))

print('保持维度')
print(np.sum(b, axis=1, keepdims=True))


print('指定数据类型（dtype）')
print(np.sum(b, axis=1, dtype=np.float32))


print('对空数组求和')
c = np.array([])
print(np.sum(c))


print('对bool数组求和')
d = np.array([True, False, True, False,True])
print(np.sum(d))
