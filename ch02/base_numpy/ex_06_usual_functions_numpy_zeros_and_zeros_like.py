import numpy as np



"""
np。zeros
创建一个填满0的数组，你可以指定形状和数据类型。
np.zeros(shape, dtype=float, order='C')
	•	shape：一个整数或元组，表示数组的形状，比如 (3, 4) 表示 3 行 4 列。
	•	dtype：可选，指定数据类型，默认是 float。
	•	order：可选，表示内存布局：'C'（行优先）或 'F'（列优先）。



"""

print('np.zeros的演示')
a = np.zeros(2)
print(a)

a1 = np.zeros((1,2))
print(a1)
a2 = np.zeros((2,3), dtype=np.float32)
print(a2)

print('np.zeros_like的演示')


"""
np.zeros_like
创建一个形状和数据类型与给定数组相同的全 0 数组。
np.zeros_like(a, dtype=None, order='K', subok=True, shape=None)
	•	a：参考的数组。
	•	dtype：可选，如果提供，则使用新的数据类型，否则和 a 一样。
	•	order：默认 'K'，尽可能保持和 a 一样的内存布局。
	•	subok：默认 True，如果为 True，返回的数组将保留子类。
	•	shape：可以指定新的形状（NumPy 1.20 后支持）。
"""
x = np.array([1,2,3])
b = np.zeros_like(x)
print(b)




















