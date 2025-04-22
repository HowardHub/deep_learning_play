import sys, os
sys.path.append(os.pardir)
import numpy as np
import matplotlib.pylab as plt



from dataset.mnist import load_mnist
from ex_06_two_layer_net import TwoLayerNet

import time



print('开始deep learning.')
# mini-batch版本
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

train_loss_list = []

#超参数
iters_num = 30000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

print('开始迭代训练，使用差分法求梯度，每迭代一次，平均耗时：5.39分钟')
for i in range(iters_num):
    print(f'第{i}次迭代')
    start_time = time.time()

    #获取mini-batch
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    #计算梯度
    #grad = network.numerical_gradient(x_batch, t_batch)
    grad = network.gradient(x_batch, t_batch)
    # grad = network.gradient(x_batch, t_batch) #高速版！

    #更新参数
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]

    #记录学习过程
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    if i == 1001 :
        end_time = time.time()
        print(f'训练十次，平均每次耗时{(end_time - start_time) / 1000}')

print(f'train_loss_len={len(train_loss_list)}')


# plt.plot(np.arange(0,iters_num), train_loss_list)
# plt.xlabel('x')
# plt.ylabel('iteration')
# plt.title('loss')

# plt.legend()
# plt.show()



# 假设 train_loss_list 已经填满了 loss 值
plt.plot(range(len(train_loss_list)), train_loss_list)
plt.xlabel('Iteration')
plt.ylabel('Training Loss')
plt.title('Training Loss over Iterations')
plt.show()



# 保存模型的参数
np.savez('two_layer_net_params.npz',
         W1=network.params['W1'],
         b1=network.params['b1'],
         W2=network.params['W2'],
         b2=network.params['b2'])
print("模型参数已保存到 two_layer_net_params.npz")


