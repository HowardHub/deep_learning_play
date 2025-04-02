import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


# 加载mnist
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# 选择训练数据的第一个数据
img = x_train[0]
label = t_train[0]
print(label) # 5


print(img.shape)          # (784,)
img = img.reshape(28, 28) # 把图像的形状变成原来的尺寸
print(img.shape)          # (28, 28)
print(img)
img_show(img)

