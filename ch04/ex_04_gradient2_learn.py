import numpy as np
import  matplotlib.pyplot  as plt





#用数值差分法，求向量x的梯度向量，1d的情况
def numerical_gradient_1d(f, x):
    h = 1e-4
    grad = np.zeros_like(x) # 生成和x一样的数组

    #for循环求每个xi偏导数
    print(x.size)
    for idx in range(x.size):
        tmpv = x[idx]

        # #f(x+h)，错误的求法。f是多变量函数，怎么只放一个值进去？
        # fx1 = f(idx + h)
        # fx2 = f(idx - h)

        #正确的求法
        x[idx] = tmpv + h
        fxh1 = f(x)
        x[idx] = tmpv - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmpv
    return grad



# 用差分法，求f的梯度，针对X为2d的情况。
def numerical_gradient(f, X):
    if X.ndim == 1:
        return numerical_gradient_1d(f, X)
    else:
        grads = np.zeros_like(X)
        for idx, x in enumerate(X):
            grads[idx] = numerical_gradient_1d(f, x)
    return grads



def function2(x):
    return x[0]**2 + x[1]** 2

print(numerical_gradient_1d(function2, np.array([3.0,4.0])))
print(numerical_gradient_1d(function2, np.array([1.0, 2.0])))





#画numerical_gradient的图像
x0 = np.arange(-2, 2.5, 0.25)
x1 = np.arange(-2, 2.5, 0.25)
X, Y = np.meshgrid(x0, x1)

X = X.flatten()
Y = Y.flatten()
print(X)
print(Y)
grad = numerical_gradient(function2, np.array([X, Y]).T).T
plt.figure()
plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666")
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('x0')
plt.ylabel('x1')
plt.grid()
plt.draw()
plt.show()










