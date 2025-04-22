import numpy as np




def numerical_gradient_1d(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmpv = x[idx]

        x[idx] = tmpv + h
        fxh1 = f(x)
        x[idx] = tmpv - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmpv
    return grad


def numerical_gradient(f, X):
    if X.ndim == 1:
        return numerical_gradient_1d(f, X)
    
    grad = np.zeros_like(X)
    for idx, x in enumerate(X):
        grad[idx] = numerical_gradient_1d(f, x)

    return grad




def gradient_descent(f, init_x, lr=0.01, step_num=100):
    """梯度下降法
    Args:
        f (_type_): 需要进行最优化的函数f
        init_x (_type_): 初始值
        lr (float, optional): 学习率. Defaults to 0.01.
        step_num (int, optional): 梯度法的重复次数. Defaults to 100.

    Returns:
        _type_: _description_
    """
    x = init_x
    for i in range(step_num):
        x -= lr * numerical_gradient(f, x)
    return x


def func1(x):
    return x[0] ** 2 + x[1] ** 2

print('只把step_num作为自变量时===================>')
#训练10次
init_x = np.array([30,20], dtype=np.float32)
print(f'初始值为{init_x}')
mini_x = gradient_descent(func1, init_x = init_x, step_num=10)
print(f'训练10次后，结果为{mini_x}')


#训练100次
init_x1 = np.array([30,20], dtype=np.float32)
print(f'初始值为{init_x1}')
mini_x1 = gradient_descent(func1, init_x = init_x1, step_num=100)
print(f'训练100次后，结果为{mini_x1}')



#训练1000次
init_x1 = np.array([30,20], dtype=np.float32)
print(f'初始值为{init_x1}')
mini_x1 = gradient_descent(func1, init_x = init_x1, step_num=1000)
print(f'训练100次后，结果为{mini_x1}')

#结论，只把step_num作为自变量时，step_num越大，越能趋近函数的最小值点。





print('只把learning_rate作为自变量时===================>')
#训练100次
init_x = np.array([30,20], dtype=np.float32)
print(f'初始值为{init_x}')
mini_x = gradient_descent(func1, init_x = init_x, lr=0.01)
print(f'训练100次后，lr=0.01，结果为{mini_x}')


init_x1 = np.array([30,20], dtype=np.float32)
print(f'初始值为{init_x1}')
mini_x1 = gradient_descent(func1, init_x = init_x1, lr=0.05)
print(f'训练100次后，lr=0.05，结果为{mini_x1}')


init_x2 = np.array([30,20], dtype=np.float32)
print(f'初始值为{init_x2}')
mini_x2 = gradient_descent(func1, init_x = init_x2, lr=0.1)
print(f'训练100次后，lr=0.1，结果为{mini_x2}')
#结论，只把lr作为自变量时，lr越大，趋近函数的最小值的速度越快

print('学习率过大的例子=========》会发散成一个很大的值')
init_x3 = np.array([30,20], dtype=np.float32)
print(f'初始值为{init_x3}')
mini_x3 = gradient_descent(func1, init_x = init_x3, lr=10.0)
print(f'训练100次后，lr=10.0，结果为{mini_x3}')


print('学习率过小的例子=========》基本上没怎么更新就结束了')
init_x4 = np.array([30,20], dtype=np.float32)
print(f'初始值为{init_x2}')
mini_x4 = gradient_descent(func1, init_x = init_x4, lr=1e-10)
print(f'训练100次后，lr=10.0，结果为{mini_x4}')



# todo，在gradient_descent中返回一个x_history列表，用来做x0,x1的图像



