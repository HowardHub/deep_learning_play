import numpy as np



"""
题目一：生成一个随机浮点数
使用NumPy生成一个介于0到1之间的随机浮点数，并打印结果。
"""
r = np.random.rand(1)
print(r)

"""
题目二：生成一维随机数组
生成一个包含5个元素的一维随机数组，元素范围为0到1之间。
"""
arr = np.random.rand(5)
print(arr)


"""
题目三：生成随机整数数组
生成一个长度为6的一维数组，每个元素是1到10（包含1和10）之间的随机整数。
"""
arr = np.random.randint(1,10,6)
print(arr)

"""
	•	问题： randint(1,10) 生成的是1到9之间的整数，不包含10。
	•	如果要包含10，正确做法应该是：randint(1,11,6)。
"""





"""
题目四：生成二维随机数组
生成一个3行4列的随机数组，元素为0到1之间的浮点数。
"""
arr2d = np.random.rand(3,4)
print(arr2d)

"""
题目五：随机整数二维数组（指定范围）
生成一个形状为3×3的随机整数数组，数值范围为10到20（包含10，不包含20）。
"""
arr2d = np.random.randint(10,20,(3,3))
print(arr2d)

"""
题目六：生成标准正态分布随机数组
生成一个长度为5的一维数组，其中元素符合标准正态分布（均值为0，方差为1）。
"""
arrn = np.random.randn(5)
print(arrn)

"""
题目七：随机数种子（seed）
先使用np.random.seed()设定随机种子为42，然后生成一个包含3个随机浮点数的一维数组（元素介于0和1之间）。
运行两次代码，观察结果是否相同。
"""
# np.random.seed(42)
# arrf = np.random.rand(3)
# print(arrf) #运行两次，结果相同


"""
题目八：随机打乱数组顺序（shuffle）
给定数组：
arr = np.array([1,2,3,4,5])
使用np.random.shuffle()随机打乱数组顺序，并打印打乱后的数组。
"""
arr = np.array([1,2,3,4,5])
np.random.shuffle(arr) #打乱顺序
print(arr)

"""
题目九：随机抽样（choice）
给定数组：
arr = np.array([10, 20, 30, 40, 50])
使用np.random.choice()从数组中随机抽取3个元素（不放回），打印抽取的结果。
"""
arr = np.array([10,20,30,40,50])
sub_arr = np.random.choice(arr, size=3)
print(sub_arr)

"""
	问题： 默认情况下，np.random.choice()是放回抽样的。题目要求不放回，应明确设置参数replace=False。
"""
sub_arr = np.random.choice(arr, size=3, replace=False)
print(f'不放回抽取：{sub_arr}')



"""
题目十：生成随机排列数组（permutation）
生成从1到10的随机排列数组，并打印结果。
"""
a = np.random.permutation(10)
print(a)
