import numpy as np


"""
np.max(x, axis=1, keepdims=True)
    x：输入的 NumPy 数组（可以是多维的）
    axis=1：指定沿哪个轴计算最大值。axis=1 表示按行方向操作（对每一列的值求最大值）
        对于二维数组，axis=0 是列方向，axis=1 是行方向。
    keepdims=True：保持输出数组的维度（维度数不变）。如果不设置（默认为 False），结果会降维

    为什么用keepdims?
        1.广播机制：保持维度后，结果可以与其他数组直接进行广播运算。例如
            x - np.max(x, axis=1, keepdims=True)
            会按行减去最大值（常见于机器学习中的归一化操作）。
        2.避免不必要的 reshape 操作。


"""


x = np.random.randn(10,2)
print(x)

x_line_direction = np.max(x, axis=1, keepdims=True)
print(f'axis=1，沿行方向求最大值。行方向的最大值：{x_line_direction}')
print(f'keepdims=True表示不降维度{x.ndim == x_line_direction.ndim}') #维度还是2D
x_line_direction = np.max(x, axis=1)
print(f'keepdims默认为false表示降维度{x.ndim == x_line_direction.ndim}') #维度变为1D


x_row_direction_max = np.max(x, axis=0, keepdims=True)
print(f'axis=0，沿列方向求最大值。列方向的最大值：{x_row_direction_max}')


