import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定

from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax
import pickle
import numpy as np

# 注意，在执行这个文件的时候，请确保terminal在ch03目录下


"""
    下面3个函数用来实现推理处理
"""

#获取测试集的数据
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label= False)
    return x_test, t_test



def init_network():
    with open('simple_weight.pkl', 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y





"""
    评价推理的精确度
"""
x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y) #获取概率最高的元素的索引
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy" + str(float(accuracy_cnt) / len(x)))
















