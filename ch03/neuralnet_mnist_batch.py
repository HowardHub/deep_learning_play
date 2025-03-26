
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定


from dataset.mnist import load_mnist
import pickle



#获取测试集的数据
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label= False)
    return x_test, t_test


x, _ = get_data()
print(x.shape)

with






