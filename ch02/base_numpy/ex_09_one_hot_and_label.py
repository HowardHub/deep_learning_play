import numpy as np




#将标签向量转为one-hot矩阵
def to_one_hot(labels, num_classes=None):
    if num_classes is None:
        num_classes = np.max(labels) + 1

    return np.eye(num_classes)[labels]




#将one-hot矩阵转为标签向量
def from_one_hot(one_hot):

    return np.argmax(one_hot, axis=1)


arr = np.array([1,2,0,3,1,2])
one_hot_list = to_one_hot(arr)
print(one_hot_list)


labels = from_one_hot(one_hot_list)
print(labels)










