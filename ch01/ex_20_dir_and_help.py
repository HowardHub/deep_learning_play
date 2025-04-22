import numpy as np


"""

为了知道模块中可以调用哪些类和函数，可以使用dir
print(dir(np))
print(dir(np.random))
在打印的结果中，忽略以‘__’开始和结束的函数（它们是python中的特殊对象）或以'_'开始的函数（通常是内容函数）




有关如何使用给定函数或类的具体说明，可以调用help函数查看
help(np.random.choice)
"""

print(dir(np.random))



help(np.random)