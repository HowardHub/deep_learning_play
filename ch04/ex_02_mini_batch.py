import sys, os
sys.path.append(os.pardir) # 为了导入父目录中的文件而进行的设定


import numpy as np
from dataset.mnist import load_mnist


(x_train, t_train),(x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)
print(x_train.shape)


# mini-batch
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
print(x_batch)
print(t_batch)
print(x_batch.shape)
print(t_batch.shape)


print(np.random.choice(60000, 10))

# help(np.random.choice)







