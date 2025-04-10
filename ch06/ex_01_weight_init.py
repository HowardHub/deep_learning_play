import numpy as np
import matplotlib.pyplot as plt
import math



'''
权重的初始值。

'''









#向一个5层神经网络（激活函数使用sigmoid函数）传入随机生成的输入数据，用直方图绘制各层激活值的数据分布
def sigmoid(x):
    return 1 / (1+np.exp(-x))

def relu(x):
    
    return np.maximum(0, x)

x = np.random.randn(1000, 100) #1000个数据点
node_num = 100 #各隐藏层的节点数
hidden_layer_size = 5 #隐藏层有5层
activations = {} #激活值的结果保存在这里


for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i-1]

    # w = np.random.randn(node_num, node_num) * 1 #各层的激活值呈偏向0和1的分布，随着输出不断地靠近0（或者靠近1）​，它的导数的值逐渐接近0。存在梯度消失的问题。
    # w = np.random.randn(node_num, node_num) * 0.01 #将权重的标准差设为0.01。输出靠近0.5，不存在梯度消失问题。
    w = np.random.randn(node_num, node_num) * np.sqrt(1 / node_num) #激活函数为sigmod或tanh时，推荐使用Xavier初始值后
    #w = np.random.randn(node_num, node_num) *  np.sqrt( 2 / node_num) #激活函数为relu时，推荐使用He初始值

    z = np.dot(x, w)
    a = sigmoid(z)
    #a = relu(z)
    activations[i] = a

#绘制直方图
for i, a  in activations.items():
    plt.subplot(1, len(activations), i+1)
    plt.title(str(i+1) + '-layer')
    plt.hist(a.flatten(), 30, range=(0,1))

plt.show()












