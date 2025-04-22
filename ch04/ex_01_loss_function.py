import numpy as np



# 均方误差损失函数；返回值越小，表示越y,t越接近。
def mean_squared_error(y, t):
    """
    Args:
        y (narray): 输出值
        t (narray): 标签值

    Returns:
        _type_: 均方误差
    """
    return 0.5 * np.sum((y-t)**2)

print('均方误差损失函数测试')
y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]) #2
t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0]) #2

a = y-t
print(a)
print(a**2)
print(0.5 * sum(a**2))
print(mean_squared_error(y, t))
#假设输出为7，
y2 = np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0,  0.6, 0.0, 0.0]) #7
print(mean_squared_error(y2, t))


#交叉熵衡量的是：模型预测的概率分布和真实分布之间有多“远”。
#如果模型预测非常接近真实标签的概率分布，交叉熵误差就很小；
#如果预测差得远，交叉熵误差就大。
#交叉墒损失函数 /ˈentrəpi/；返回值越小，表示越y,t越接近。
def cross_entropy_error(y, t):
    delta = 1e-7
    return -1 * np.sum(t * np.log(y + delta)) #防止出现np.log(0)时，np.log(0)会变为负无限大的-inf


print('交叉墒误差损失函数测试')


t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] #2
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0] #2
print(cross_entropy_error(np.array(y), np.array(t)))

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0] #7
print(cross_entropy_error(np.array(y), np.array(t)))








