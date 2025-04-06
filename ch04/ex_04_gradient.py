import sys, os
sys.path.append(os.pardir) # 为了导入父目录中的文件而进行的设定

from common.functions import function_2


import numpy as np

"""
梯度：由全部变量的偏导数汇总而成的向量称为梯度

性质：梯度指示的方向是各点处的函数值减小最多的方向
"""



#求f在x处的梯度向量
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x) #生成和x形状相同且所有元素全为0的数组

    for idx in range(x.size):
        tmp_val = x[idx]
        #f(x+h)的计算
        x[idx] = tmp_val + h
        fxh1 = f(x)

        #f(x-h)的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val #还原值

    #返回梯度数组
    return grad




print(numerical_gradient(function_2, np.array([3.0, 4.0]))) #输出[6.0, 8.0]
print(numerical_gradient(function_2, np.array([0.0, 2.0]))) #输出[0, 4.0]


#梯度下降法更新x
#学习率是超参数，需要进行多次尝试，以便找到一种可以使学习顺利进行的设定
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x




#用梯度法求function2的最小值点
init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100))



#学习率过大的例子：lr=10
init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x=init_x, lr=10.0, step_num= 100))


#学习率过小的例子：lr=1e-10
init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x=init_x, lr=1e-10, step_num=100))











