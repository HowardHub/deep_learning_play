# from abc import ABC, abstractclassmethod
# 第7题，注意导入应为from abc import ABC, abstractmethod。
from abc import ABC, abstractmethod



"""
📌 题目 1：定义一个类
	1.	定义一个 Person 类，包含：
	•	name（姓名）和 age（年龄）两个实例变量。
	•	一个 __init__ 方法用于初始化 name 和 age。
	•	一个 introduce 方法，返回 "我是 XXX，今年 YYY 岁"（XXX 和 YYY 分别是姓名和年龄）。
	2.	创建一个 Person 对象，并调用 introduce 方法。
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f'我是{self.name}，今年{self.age}岁'
    
person = Person('张山', 18)
print(person.introduce())




"""
📌 题目 2：封装
	1.	修改 Person 类：
	•	让 age 变成私有属性（私有变量）。
	•	提供 get_age 和 set_age 方法，分别用于获取和修改年龄，但要求年龄必须是正整数。
	2.	进行测试：
	•	先打印 age（应报错）。
	•	使用 get_age() 获取 age。
	•	使用 set_age(-1) 观察是否会报错。
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age <= 0:
            raise ValueError('年龄必须为正数')
        self.__age = age



person = Person('张三', 18)
print(person.__age)
print(person.get_age())
person.set_age(-1)



"""
📌 题目 3：类方法和静态方法
	1.	在 Person 类中：
	•	定义一个类变量 species = "Human"。
	•	定义一个类方法 get_species()，返回 species。
	•	定义一个静态方法 is_adult(age)，如果 age >= 18 返回 True，否则返回 False。
	2.	进行测试：
	•	直接通过 Person 类调用 get_species() 和 is_adult()。
"""
class Person:
    species = 'Human'

    def get_species(self):
        return self.species
    
    @staticmethod
    def is_adult(age):
        return age >= 18

person = Person()
print(person.get_species())
print(Person.is_adult(3))

"""
	•	你的类方法定义缺少装饰器@classmethod，参数缺少cls。

    @classmethod
    def get_species(cls):
        return cls.species
"""





"""
📌 题目 4：继承
	1.	定义一个 Student 类，继承 Person：
	•	增加 grade（年级）属性。
	•	重写 introduce 方法，返回 "我是 XXX，今年 YYY 岁，在读 ZZZ 年级"。
	2.	创建 Student 对象，并调用 introduce 方法。
"""
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f'我是{self.name}，今年{self.age}岁'


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age) #调用父类的init方法时，不用self方法
        self.grade = grade

    def introduce(self):
        return f'我是{self.name}，今年{self.age}岁，在读{self.grade}年级'
    
student = Student('李四', 28, 9)
print(student.introduce())





"""
📌 题目 5：方法重载（多态）
	1.	在 Person 类中：
	•	定义一个 speak 方法，打印 "我会说话"。
	2.	在 Student 类中：
	•	重写 speak 方法，打印 "我是学生，我在学习"。
	3.	创建 Person 和 Student 实例，分别调用 speak()。
"""
class Person:
    def speak(self): #即使你不使用这个参数，也需要在方法定义中包含它。
        print('我会说话')

class Student(Person):
    def speak(self): #实例方法的第一个参数必须是 self，它代表类的实例本身。
        print('我是学生，我在学习')

person = Person()
student = Student()

person.speak()
student.speak()



"""
📌 题目 6：运算符重载
	1.	在 Person 类中：
	•	重载 __str__ 方法，使 print(Person("张三", 25)) 输出 "姓名: 张三, 年龄: 25"。
	•	重载 __lt__ 方法，使 p1 < p2 比较 age（年龄小的算更小）。
	2.	进行测试：
	•	创建两个 Person 对象并进行比较。
"""
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'姓名: {self.name}, 年龄: {self.age}'
    
    def __lt__(self, p2):
        return self.age < p2.age
    
p1 = Person('张山', 15)
p2 = Person('李四', 18)

print(p1)
print(p1.__lt__(p2))
print(p1 < p2) #自动调用__lt__()

"""
	•	比较时，通常直接写print(p1 < p2)更好，Python会自动调用__lt__方法。


"""



"""
📌 题目 7：抽象类
	1.	导入 ABC 和 abstractmethod，创建一个抽象类 Animal：
	•	定义 speak 作为抽象方法。
	2.	让 Dog 和 Cat 继承 Animal 并实现 speak：
	•	Dog 的 speak() 返回 "汪汪！"。
	•	Cat 的 speak() 返回 "喵喵！"。
	3.	测试 Dog 和 Cat 的 speak()。
"""
class Animal(ABC):
    @abstractmethod
    def speak(self):
        """子类必须实现这个方法"""
        pass
class Dog(Animal):
    def speak(self):
        return '汪汪！'

class Cat(Animal):
    def speak(self):
        return '喵喵！'
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())

"""
存在问题：
	•	你的装饰器使用错误，应使用@abstractmethod，而非@abstractclassmethod。
	•	注意导入应为from abc import ABC, abstractmethod。
"""







"""
📌 题目 8：类变量与实例变量
	1.	在 Person 类中：
	•	添加一个类变量 count，记录创建的 Person 实例数量。
	•	在 __init__ 方法中，每次创建实例时 count += 1。
	2.	进行测试：
	•	创建多个 Person 对象，并打印 Person.count。
"""
class Person(): #是class Person，而不是def Person
    count = 0
    def __init__(self):
        Person.count += 1 #是Person.count，而不是self.count

p1 = Person()
p2 = Person()
p3 = Person()
print(Person.count)




"""
📌 题目 9：单例模式
	1.	使用 单例模式 设计 Database 类：
	•	只能创建 一个 Database 实例。
	•	如果已有实例，__new__ 方法应返回已有实例，而不是创建新的。
	2.	进行测试：
	•	尝试创建多个 Database 对象，验证它们的 id() 是否相同。
"""
class Database:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    

    def __init__(self, value):
        if not hasattr(self, 'value'):
            self.value = value

instance1 = Database()
instance2 = Database()

print(instance1.id())
print(instance2.id())

"""
存在问题：
	•	你调用了instance1.id()，但Python获取对象ID的方式应为内置函数id(instance)，对象本身没有id()方法。
	•	你创建实例时，没有传入value参数，但__init__要求必须传入。

"""
class Database:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value=None):
        if not hasattr(self, 'value'):
            self.value = value

instance1 = Database('MySQL')
instance2 = Database('Postgres')

print(id(instance1))
print(id(instance2))
print(instance1.value)  # 应输出 MySQL，证明第二次初始化未生效







"""
📌 题目 10：组合
	1.	定义 Engine 类：
	•	属性 power（功率）。
	•	方法 start() 返回 "发动机启动，功率：XXX"。
	2.	定义 Car 类：
	•	具有 brand（品牌）和 engine（发动机）两个属性。
	•	方法 start() 依赖 engine.start()。
	3.	进行测试：
	•	创建 Car 对象并启动汽车。
"""

class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        return f'发动机启动，功率：{self.power}'



class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine
    def start(self):
        return self.engine.start() #这里是需要return的，不然会返回None

car = Car('Tesla', Engine('1000KW'))
print(car.start())





