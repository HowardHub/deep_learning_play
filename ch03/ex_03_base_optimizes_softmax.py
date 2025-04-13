import numpy as np


'''
假设输入的是n个数据，也就是x.shape=(n,2)，
要保证softmax后，每一行的求和结果为1，需要对softmax进行改造。
1.分别找到每行的最大值
2.分别对每行求和
3.分别求softmax
'''


def sigmoid(x):
    return 1 / (1 + np.exp(-x))



def softmax(x):
    c = np.max(x, axis=1, keepdims=True) #对每行求最大值
    exp_x = np.exp(x - c) #防止溢出
    sum_exp_x = np.sum(exp_x, axis=1, keepdims=True) #对每行求和
    return exp_x / sum_exp_x




class SimpleNetwork:

    '''
    输入.shape=(n,2)
    W1.shape=(2,3)
    W2.shape=(3,2)
    W3.shape=(2,2)
    输出.shape=(n,2)

    '''
    def __init__(self):
        self.params = {}
        self.params['W1'] = np.random.randn(2,3)
        self.params['b1'] = np.random.randn(3)
        self.params['W2'] = np.random.randn(3,2)
        self.params['b2'] = np.random.randn(2)
        self.params['W3'] = np.random.randn(2,2)
        self.params['b3'] = np.random.randn(2)

    #前向传播
    def forward(self, x):
        a1 = np.dot(x, self.params['W1']) + self.params['b1']
        z1 = sigmoid(a1)
        a2 = np.dot(z1, self.params['W2']) + self.params['b2']
        z2 = sigmoid(a2)
        a3 = np.dot(z2, self.params['W3']) + self.params['b3']

        out = softmax(a3)
        return out


simpleNetwork = SimpleNetwork()
x = np.random.randn(10,2) #造10个数据
y = simpleNetwork.forward(x)
print(y)



print(np.sum(y, axis=1))









