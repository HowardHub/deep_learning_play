import numpy as np

import sys, os
sys.path.append(os.pardir) # 为了导入父目录中的文件而进行的设定
from dataset.mnist import load_mnist
import pickle




"""
单层神经网络处理MNIST

网络结构
输入层有784个神经元，
第一个隐藏有50个神经元
第二个隐藏层有100个神经元
输出层有10个神经元




#调用
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)时，为啥这么命名x_train，t_train？

x 表示输入数据（特征）；x 是数学中常用的自变量符号，在机器学习中，x 通常代表输入数据（features，特征），即模型的输入变量。
t 表示目标数据（标签）；t 通常代表 "target"（目标值），即模型要预测的变量（label，标签），在监督学习中，t 是训练数据的真实标签（ground truth）。
train 表示训练集（用于训练模型）。
test 表示测试集（用于评估模型性能）。
例如，对于x_train，从后往前读train训练，x数据，所以x_train训练数据；
     对于t_test，从后往前读，test测试，t标签，所以t_test测试标签。
tips：有的教材中t会被换成y，y_train,y_test


"""

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    c = np.max(x, axis=1, keepdims=True)
    exp_x = np.exp(x - c)
    sum_exp_x = np.sum(exp_x, axis=1, keepdims=True) #对每行求和，保持维度不变
    return exp_x / sum_exp_x




# def softmax(x):
#     c = np.max(x)
#     exp_x = np.exp(x - c)
#     sum_exp_x = np.sum(exp_x)
#     return exp_x / sum_exp_x


class SingleLayerNetworkMnist:


    def __init__(self, trained=True):
        #初始化权重参数
        self.params = {}
        if trained:
            #使用训练好的网络
            network = self.load_params()
            self.params['W1'] = network['W1']
            self.params['b1'] = network['b1']
            self.params['W2'] = network['W2']
            self.params['b2'] = network['b2']
            self.params['W3'] = network['W3']
            self.params['b3'] = network['b3']
        else:
            #使用未训练的网络
            self.params['W1'] = np.random.randn(784, 50)
            self.params['b1'] = np.random.randn(50)
            self.params['W2'] = np.random.randn(50, 100)
            self.params['b2'] = np.random.randn(100)
            self.params['W3'] = np.random.randn(100, 10)
            self.params['b3'] = np.random.randn(10)


    def load_params(self):
        with open('simple_weight.pkl', 'rb') as f:
            network = pickle.load(f)
        return network

    #获取MNIST数据
    def get_data(self):
        (x_train, t_train), (x_test, t_test) = load_mnist(one_hot_label=False)
        return (x_test, t_test)

    #推理
    def predict(self, x_test):

        a1 = np.dot(x_test, self.params['W1']) + self.params['b1']
        z1 = sigmoid(a1)
        a2 = np.dot(z1, self.params['W2']) + self.params['b2']
        z2 = sigmoid(a2)
        a3 = np.dot(z2, self.params['W3']) + self.params['b3']
        z3 = softmax(a3)
        return z3




# network = SingleLayerNetworkMnist(trained=True)
# x_test, t_test = network.get_data()
# accuracy_cnt = 0
# for i in range(len(x_test)):
#     y = network.predict(x_test[i])
#     p = np.argmax(y) #获取概率最高的索引
#     #print(f'test[i]={t_test[i]}')
#     if p == t_test[i]:
#         accuracy_cnt += 1
# y = network.predict(x_test)
# print(f'使用训练好的网络，准确率：{str(100 * float(accuracy_cnt)/ len(x_test))}%')


# accuracy_cnt = 0
# network = SingleLayerNetworkMnist(trained=False)
# for i in range(len(x_test)):
#     y = network.predict(x_test[i])
#     p = np.argmax(y) #获取概率最高的索引
#     #print(f'test[i]={t_test[i]}')
#     if p == t_test[i]:
#         accuracy_cnt += 1
# print(f'使用未训练的网络，准确率：{str(100 * float(accuracy_cnt)/ len(x_test))}%')





# numpy.argmax(a, axis=None, out=None)
# network = SingleLayerNetworkMnist(trained=True)
# x_test, t_test = network.get_data()
# y = network.predict(x_test)
# print(y.shape)
# print(t_test.shape)
# y_max = np.argmax(y, axis=1)
# print(y_max.shape)
# print(y_max)
# print(t_test)
# count = np.sum(y_max == t_test)
# print(f'全处理，使用训练好的网络，准确率：{str(100 * float(count)/ len(x_test))}%')





network = SingleLayerNetworkMnist(trained=True)
x_test, t_test = network.get_data()
accuracy_cnt = 0
batch_size = 100
for i in range(0, len(t_test), batch_size):
    y = network.predict(x_test[i : i + batch_size])
    p = np.argmax(y, axis=1) # 获取概率最高的索引
    accuracy_cnt += np.sum(p == t_test[i:batch_size+i])

print(f'batch_size = 100，批处理，使用训练好的网络，准确率：{str(100 * float(accuracy_cnt)/ len(x_test))}%')





