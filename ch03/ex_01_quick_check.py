import numpy as np


def _change_one_hot_label(X):
    print(f'打印一个x[0]= {X[0]}')
    T = np.zeros((X.size, 10))
    for idx, row in enumerate(T):
        row[X[idx]] = 1
        
    return T


X = np.array([4,2,9])
res = _change_one_hot_label(X)
print(X)
print(res)






