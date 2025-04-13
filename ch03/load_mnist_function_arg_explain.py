import sys, os
sys.path.append(os.pardir) # 为了导入父目录中的文件而进行的设定
from dataset.mnist import load_mnist

# 第一次调用会花费几分钟……
# (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# 输出各个数据的形状
# print(x_train.shape) # (60000, 784)，60000张训练图片，784表示图片由28*28的二维转为一维784
# print(t_train.shape) # (60000,)
# print(x_test.shape) # (10000, 784)
# print(t_test.shape) # (10000,)


#normalize验证
# 第1个参数normalize设置是否将输入图像正规化为0.0～1.0的值。如果将该参数设置为False，则输入图像的像素会保持原来的0～255
# (x_train, t_train), (x_test, t_test) = load_mnist(normalize = False)
# print(type(x_train))
# print(x_train[0]) #没有归一化，输出有0～255的数值


# (x_train, t_train), (x_test, t_test) = load_mnist(normalize = True)
# print(x_train[0]) #归一化，输出全是0～1的数值


#第2个参数flatten设置是否展开输入图像（变成一维数组）​。
#如果将该参数设置为False，则输入图像为1×28×28的三维数组；
#若设置为True，则输入图像会保存为由784个元素构成的一维数组
# (x_train, t_train), (x_test, t_test) = load_mnist(flatten = True)
# x1 = x_train[0]
# print(x1) #展开图像
# print(x1.shape) #(784,)
# print(x1.ndim) #1维


# (x_train, t_train), (x_test, t_test) = load_mnist(flatten = False)
# x1 = x_train[0]
# print(x1) #不展开图像
# print(x1.shape) #(1,28,28)
# print(x1.ndim) #3维




#第3个参数one_hot_label设置是否将标签保存为one-hot表示(one-hot representation)。
#one-hot表示是仅正确解标签为1，其余皆为0的数组，就像[0,0,1,0,0,0,0,0,0,0]这样。
#当one_hot_label为False时，只是像7、2这样简单保存正确解标签；当one_hot_label为True时，标签则保存为one-hot表示

# (x_train, t_train), (x_test, t_test) = load_mnist(one_hot_label=True) #设置为one_hot标签
# t1 = t_train[0]
# print(type(t1))#<class 'numpy.ndarray'>
# print(t1) #[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]


# (x_train, t_train), (x_test, t_test) = load_mnist(one_hot_label=False) #不设置为one_hot标签
# t1 = t_train[0]
# print(type(t1)) #<class 'numpy.uint8'>
# print(t1) #[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]







