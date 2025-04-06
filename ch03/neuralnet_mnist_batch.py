
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定


from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax
import pickle
import numpy as np


#获取测试集的数据
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label= False)
    return x_test, t_test

def init_network():
    with open('simple_weight.pkl', 'rb') as f:
        network = pickle.load(f) #用pickle把f加载成模型
        return network


# X即使是批处理数据，网络结构和预测结构与对单个数据的处理时是一样的。
def predict(network, X):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(X, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3

    y = softmax(a3)
    return y
 

x, t = get_data()

network = init_network()
batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i + batch_size]
    y_batch = predict(network, x_batch)
    #print(f'x_batch.shape={x_batch.shape}')
    #print(f'y_batch.shape = {y_batch.shape}')
    p = np.argmax(y_batch, axis=1)
    #print(f'p.shape = {p.shape}')
    accuracy_cnt += np.sum(p == t[i : i+batch_size])

print(f'精确率：{float(accuracy_cnt) / len(x)}')









