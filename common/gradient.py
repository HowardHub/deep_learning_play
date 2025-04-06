import numpy as np




#自己写的版本
#求f在x处的梯度向量
# def numerical_gradient(f, x):
#     h = 1e-4
#     grad = np.zeros_like(x) #生成和x形状相同且所有元素全为0的数组

#     #为了对应形状为多维数组的权重参数W，这里使用的numerical_gradient()和之前的ex_04_gradient.py实现稍有不同。
#     #不过，改动只是为了对应多维数组.
#     for i in range(x.shape[0]):     # 遍历行
#         for j in range(x.shape[1]): # 遍历列
#             tmp_val = x[i][j]
#             #计算f(x+h)
#             x[i][j] = tmp_val + h
#             fxh1 = f(x)

#             #计算f(x-h)
#             x[i][j] = tmp_val - h
#             fxh2 = f(x)

#             grad[i][j] = (fxh1 - fxh2) / (2*h)
#             x[i][j] = tmp_val
#     #返回梯度数组
#     return grad




#书上的版本
def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 値を元に戻す
        it.iternext()   
        
    return grad









