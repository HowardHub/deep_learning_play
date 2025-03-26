import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 从输入层到第一层的信号传递
X = np.array([1, 2])
W1 = np.array([[0.1, 0.2, 0.33], [0.4,0.5,0.6]])
B1 = np.array([0.1, 0.2, 0.3])

A1 = np.dot(X, W1) + B1
print('第1层参数')
print(f'X.shape={X.shape}')
print(f'W1.shape={W1.shape}')
print(f'B1.shape={B1.shape}')
print(f'A1.shape={A1.shape}')

# 第一层的加权和经过激活函数
Z1 = sigmoid(A1)
print(f'第1层输出结果Z1={Z1}')

# 第一层到第二层之前的信号传递
W2 = np.array([[1,2], [3,4],[5,6]])
B2 = np.array([0.1, 0.2])
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print('第2层参数：')
print(f'Z1.shape={Z1.shape}')
print(f'W2.shape={W2.shape}')
print(f'B2.shape={B2.shape}')
print(f'A2.shape={A2.shape}')
print(f'第2层输出结果Z2={Z2}')



# 定义最后一层的激活函数，恒等函数
def identity_function(x):
    return x

W3 = np.array([[1,2], [3,4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)

print('第3层参数：')
print(f'Z2.shape={Z2.shape}')
print(f'W3.shape={W3.shape}')
print(f'B3.shape={B3.shape}')
print(f'A3.shape={A3.shape}')
print(f'第3层输出结果Y={Y}')





"""把网络结构用函数定义起来
    按照神经网络的实现惯例，只把权重记为大写字母W1，其他的（偏置或中间结果等）都用小写字母表示
    init_network()函数会进行权重和偏置的初始化，并将它们保存在字典变量network中
"""
def init_network():
    network = {}
    W1 = np.array([[0.1, 0.2, 0.33], [0.4,0.5,0.6]])
    network['W1'] = W1
    b1 = np.array([0.1, 0.2, 0.3])
    network['b1'] = b1

    W2 = np.array([[1,2], [3,4],[5,6]])
    network['W2'] = W2
    network['b2'] = np.array([0.1, 0.2])

    W3 = np.array([[1,2], [3,4]])
    network['W3'] = W3
    network['b3'] = np.array([0.1, 0.2])

    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    z1 = sigmoid(np.dot(x, W1) + b1)
    z2 = sigmoid(np.dot(z1, W2) + b2)
    y = identity_function(np.dot(z2, W3) + b3)
    return y



# 调用
x = np.array([1,2])
network = init_network()
y = forward(network, x)
print(y)









