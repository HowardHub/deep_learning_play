import numpy as np



#SGD优化器
class SGD:
    """
        SGD低效的根本原因是，梯度的方向并没有指向最小值的方向。

    """
    def __init__(self, lr = 0.01):
        self.lr = lr

    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]



#Momentum参照小球在碗中滚动的物理规则进行移动
class Momentum:

    def __init__(self, lr = 0.01, momentum = 0.9):
        self.lr = lr
        self.v = None
        self.momentum = momentum

    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)

        for key in params.keys():
            self.v[key] = self.momentum * self.v[key] - self.lr * grads[key]
            params[key] += self.v[key]




#AdaGrad为参数的每个元素适当地调整更新步伐
class AdaGrad:

    def __init__(self, lr = 0.01):
        self.lr = lr
        self.h = None


    def update(self, params, grads):
        if self.h is None:
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)

        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key] + 1e-7))


#融合了Momentum和AdaGrad的优点
class Adam:
    pass