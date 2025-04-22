import numpy as np

class Relu:

    def __init__(self):
        self.mask = None

    
    def forward(self, x):
        # 将<=0 的元素设为0
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out
    

    def backward(self, dout):
        # 将mask为true的部分置为0，否则原样输出。
        dout[self.mask] = 0 
        dx = dout
        return dx
    
# relu = Relu()
# x = np.array([1,0,3])
# print(relu.forward(x))
# print(relu.backward(np.array([-1,2,2])))




class Affine:

    def __init__(self, W, b):
        self.W = W
        self.b = b

        self.X = None
        self.dW = None
        self.db = None
        self.orinial_shape = None


    def forward(self, x):
        self.orinial_shape = x.shape
        x = x.reshape(x.shape[0], -1)

        self.X = x
        out = np.dot(x, self.W) + self.b
        return out


    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.X.T, dout)
        self.db = np.sum(dout, axis=0)
        dx = dx.reshape(*self.orinial_shape)
        return dx
    



W = np.array([[1,1,1],[2,1,2]])
b = np.array([1,2,3])
affine  = Affine(W, b)
x = np.array([[1,2],[2,1]])
out = affine.forward(x)
print(out)

dout = np.array([[1,2,1],[2,1,2]])
dx = affine.backward(dout)
print(dx)



def softmax(x):
    x = x - np.max(x, axis=-1, keepdims=True)  
    return np.exp(x) / np.sum(np.exp(x), axis=-1, keepdims=True)

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    if t.size == y.size:
        t = t.argmax(axis=1)
             
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size

class SoftmaxWithLoss:

    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None


    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        out = cross_entropy_error(self.y, t)
        self.loss = out
        return out
    





    def backward(self, dout=1):

        pass







class TwoLayersNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std):
        pass




    def predict(self, x):
        pass




    def backward(self, dout):
        pass



    def loss(self, x, t):
        pass



    def accuarcy(self, x, t):
        pass





    def gradient(self, x, t):

        pass









