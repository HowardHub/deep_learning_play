import numpy as np


#将每行的数据变成概率，且和为1
def softmax(x):
    #向量情况
    if x.ndim == 1:
        c = np.max(x)
        exp_x = np.exp(x - c)
        sum_exp_x = np.sum(exp_x)
        return exp_x / sum_exp_x
    c = np.max(x, axis=1, keepdims= True)
    exp_x = np.exp(x -c)
    sum_exp_x = np.sum(exp_x, axis=1, keepdims=True)
    return exp_x / sum_exp_x





def cross_entropy_error(y, t):
    #兼容单个数据
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)
    batch_size = y.shape[0]
    delta = 1e-7
    #因为是求和的操作，所以不需要指定axis。对y求对数，然后把y和t相乘得到一个ndim,shape相同的数据，再对数组进行求和。
    return -np.sum(t * np.log(y + delta)) / batch_size #可以在脑海里复现这个计算过程。
    

# 梯度
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





class SimpleNet:

    def __init__(self):
        self.W = np.random.randn(2,3)

    
    def forward(self,x):
        return np.dot(x, self.W)
    

    def loss(self, x, t):
        z = self.forward(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss


    
net = SimpleNet()
print(f'网络初始化参数W：{net.W}')
x = np.array([0.6, 0.6])
t= np.array([0,0,1])
p = net.forward(x)
print(f'前向传播的输出值p:{p}')
print(f'最大索引值{np.argmax(p)}')


#损失函数
def f(W):
    #W是个伪参数，numerical_gradient(f, x)会在内部执行f(x)，为了与之兼容而定义了f(W)）​。
    return net.loss(x, t)





#求解损失函数关于参数的梯度
#假设grad的第一个值为0.1，它表示W11增加h，那么损失函数的值就会增加0.1h
#假设grad的第二个值为-0.3，它表示W11增加h，那么损失函数的值就会减少0.3h
grad = numerical_gradient(f, net.W)
print(f'损失函数的关于W的梯度:{grad}')

#todo：得到梯度后，就需要用梯度下降法，更新W










