import numpy as np



"""
numpy.argmax(a, axis=None, out=None)
a：输入的数组。
axis（可选）：指定沿哪个轴查找最大值索引。如果不指定（axis=None），函数会将数组展平（flatten）后返回全局最大值的索引。
axis=0：沿列方向（逐列查找最大值索引）。
axis=1：沿行方向（逐行查找最大值索引）。
out（可选）：用于存放结果的输出数组（一般不常用）。


返回一个包含最大值索引的数组。如果指定了 axis，则结果的形状是输入数组去掉指定轴后的形状；如果不指定 axis，则返回一个标量（展平后的索引）。



"""





arr = np.array([[1,2,3], [6,1,4]])
max_line_index = np.argmax(arr, axis=1)
print(max_line_index) #[2 0]
max_row_index = np.argmax(arr, axis=0)
print(max_row_index) #[1 0 1]















