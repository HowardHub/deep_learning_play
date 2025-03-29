"""
一、迭代器
1. 什么是迭代器？
迭代器是一个可以记住遍历位置的对象。它实现了两个核心方法：__iter__() 和 __next__()，
允许你逐个访问容器（如列表、字典等）中的元素，而无需提前加载所有数据到内存。

核心特点：
    惰性计算：按需生成数据，节省内存。
    单向遍历：只能前进，不能后退。
    一次性使用：遍历结束后，再次使用需重新创建。


2. 迭代器 vs 可迭代对象
可迭代对象 (Iterable)：任何可以用 for 循环遍历的对象（如列表、元组、字符串）。
    必须实现 __iter__() 方法，返回一个迭代器。
迭代器 (Iterator)：实现了 __iter__() 和 __next__() 的对象。
    __iter__() 返回自身。
    __next__() 返回下一个元素，无元素时抛出 StopIteration 异常。   

    
3. 迭代器的工作原理
Python 的 for 循环底层就是通过迭代器实现的：
调用 iter() 获取对象的迭代器。
循环调用 next() 获取元素，直到捕获 StopIteration 异常。 


4. 如何自定义迭代器？
通过类实现 __iter__() 和 __next__() 方法。
    


"""





"""
📌 题目 1：自定义迭代器基础
定义一个名为 Counter 的迭代器类，从 1 开始，每次调用返回下一个整数，最多返回到 5。
"""
class Counter:
    def __init__(self):
        self.max = 5
        self.init = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.init < 5:
            self.init += 1
            return self.init
        else:
            raise StopIteration


# 测试代码
counter = Counter()
for num in counter:
    print(num)









"""
📌 题目 3：迭代器实现斐波那契数列
定义一个名为 Fibonacci 的迭代器类，用于产生前 n 个斐波那契数（0, 1, 1, 2, 3, 5, 8…）。
"""
class Fibonacci:
    def __init__(self, max_num):
        self.a = 0
        self.b = 1
        self.max_num = max_num

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a > self.max_num:
            raise StopIteration
        res = self.a
        self.a, self.b = self.b, self.a + self.b
        return res        


# 测试代码
fib = Fibonacci(7)
for num in fib:
    print(num, end=' ')

print()







"""
📌 题目 5：迭代器实现无限偶数序列（带停止条件）
定义一个名为 EvenNumbers 的迭代器类，每次调用生成下一个偶数（从2开始），但最多生成到指定的最大数为止。
"""
class EvenNumbers:
    def __init__(self, max_odd): # odd奇数，even偶数
        self.cur_odd = 2
        self.max_odd = max_odd

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur_odd > self.max_odd:
            raise StopIteration
        res = self.cur_odd
        self.cur_odd += 2
        return res


# 测试代码
evens = EvenNumbers(10)
for num in evens:
    print(num, end=' ')




