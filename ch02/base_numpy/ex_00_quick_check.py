import numpy as np


eye = np.eye(4)

print(eye)


labels = np.array([0, 2, 1, 3, 2, 0])


'''
a = eye[labels] 等价于：

a = np.array([
    eye[0],   # 取第 0 行
    eye[2],   # 取第 2 行
    eye[1],   # 取第 1 行
    eye[3],   # 取第 3 行
    eye[2],   # 再取第 2 行
    eye[0]    # 再取第 0 行
])

'''
a = eye[labels] #用labels数组作为索引，从eye这个4x4矩阵中按顺序取出对应的行

print(a)




def to_one_hot(labels, num_classes=None):
    if num_classes is None:
        num_classes = np.max(labels) + 1


    return np.eye(num_classes)[labels]


labels = np.array([0, 2, 1, 3, 2, 0])

one_hot_list = to_one_hot(labels)
print(one_hot_list)




def from_one_hot(one_hot):
    return np.argmax(one_hot, axis=1)


ls = from_one_hot(one_hot_list)
print(ls)





