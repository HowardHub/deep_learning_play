import numpy as np




#x是1d的
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



# X可以是2D的，也可以是1D的，看作是对向量的批处理版本
def numerical_gradient(f, X):
    if X.ndim == 1:
        return numerical_gradient_1d(f, X)
    grad = np.zeros_like(X)

    for idx, x in enumerate(X):
        grad[idx] = numerical_gradient_1d(f, x)

    return grad


def fun1(x):
    return x[0] ** 2 + x[1] ** 2


def fun2(x):
    return x[0] ** 2 + x[1] ** 2 + 2 * x[2]





print('针对fun1，numerical_gradient_1d测试===============>：')
x = np.array([1, 2], dtype=np.float32)
print(f'当x是{x}时，它的梯度是{numerical_gradient_1d(fun1, x)}')
x = np.array([2, 3], dtype=np.float32)
print(f'当x是{x}时，它的梯度是{numerical_gradient_1d(fun1, x)}')

print('\n针对fun1，numerical_gradient测试： ')
X = np.array([[1,2], [2,3]], dtype=np.float32)
print(f'当x是：\n{X}时，它的梯度是\n{numerical_gradient(fun1, X)}')



print('针对fun2，numerical_gradient_1d测试=================>：')
x = np.array([1, 2,3], dtype=np.float32)
print(f'当x是{x}时，它的梯度是{numerical_gradient_1d(fun2, x)}')
x = np.array([2, 3,1], dtype=np.float32)
print(f'当x是{x}时，它的梯度是{numerical_gradient_1d(fun2, x)}')

print('\n针对fun2，numerical_gradient测试： ')
X = np.array([[1,2,3], [2,3,1]], dtype=np.float32)
print(f'当x是：\n{X}时，它的梯度是\n{numerical_gradient(fun2, X)}')








