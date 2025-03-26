
import numpy as np


def identity_function(x):
    return x


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #防止溢出
    # 为了防止sum_exp_a太大，从而造成溢出，把每一个元素减去数组中的最大值，让和在一个小范围呢i
    sum_exp_a = sum(exp_a)
    y = exp_a / sum_exp_a
    return y








