## 损失函数部分的要求
* 1.实现单变量、向量、矩阵、张量版本的均方误差和交叉墒损失函数
* 2.实现1的mini-batch版本



## 梯度部分的要求
* 1.会实现 def numerical_gradient_1d(f, x)
* 2.会实现 def numerical_gradient(f, X)
* 3.会实现 def gradient_descent(f, init_x, lr=0.01, step_num=100)




## 定义网络结构相关要求
* 1.会实现def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01)
* 2.会实现def forward(self, x)
* 3.会实现def loss(self y, t)
* 4.会实现def numerical_gradient(f, x)
* 5.会实现def accuracy(self, x, t)




## 网络训练相关的要求
* 1.理解训练的4步骤
  * 1.获取mini-batch数据
  * 2.计算梯度
  * 3.通过梯度下降法更新参数
  * 重复1，2，3
