import numpy as np


"""优化版
把参数放在params字典中，激活函数采用softmax


softmax函数的输出值的总和是1。输出总和为1是softmax函数的一个重要性质。
正因为有了这个性质，我们才可以把softmax函数的输出解释为“概率.


一般而言，神经网络只把输出值最大的神经元所对应的类别作为识别结果。
并且，即便使用softmax函数，输出值最大的神经元的位置也不会变。
因此，神经网络在进行分类时，输出层的softmax函数可以省略。
在实际的问题中，由于指数函数的运算需要一定的计算机运算量，因此输出层的softmax函数一般会被省略。



输出层激活函数怎么确定？
根据求解问题的性质决定：
回归问题，用恒等函数、二元分类问题用sigmoid函数，多元分类用softmax函数。

"""

def sigmoid(x):
    return 1 / (1 + np.exp(-x))



def softmax(x):
    c = np.max(x)
    exp_x = np.exp(x - c) #防止溢出
    sum_exp_x = np.sum(exp_x)
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



print(np.sum(y)) #问题，如果x.shape(10,2)，输出的y为何不是一行的结果为1，而是所有的结果为1？










