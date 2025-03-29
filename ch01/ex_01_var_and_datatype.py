#这些题目都是由ChatGPT老师出的，详情请看https://chatgpt.com/share/67e39e82-271c-8003-b241-aabe2d2ce048


#1.定义三个变量 name、age 和 height，分别表示你的名字（字符串）、年龄（整数）和身高（浮点数）。
#然后用 print() 语句输出这些变量，并确保数据类型正确。
name = 'hizhipeng'
age = 18
height = 188.8
print(f'姓名：{name}')
print(f'年龄：{age}')
print(f'身高：{height}')

#2.编写一个 Python 程序，要求用户输入两个数字（字符串类型），然后将它们转换为整数，并计算它们的和、差、积、商（保留两位小数）。
num1 = input('请输入第一个数字: ')
num1 = int(num1)
num2 = input('请输入第二个数字：')
num2 = int(num2)
# 改进用，if num1.isdigit() and num2.isdigit():  # 确保输入的是数字
print(f'和：{num1 + num2}')
print(f'差：{num1 - num2}')
print(f'积：{num1 * num2}')
print(f'商：{(num1 / num2):.2f}')

# 3.定义两个变量 a 和 b，赋值为任意两个整数。然后交换它们的值并打印输出 （不能使用第三个变量）。
a = 10
b = 4
a, b = b, a #不使用第3个变量来交换两个变量
print(f'a={a}')
print(f'b={b}')

#4.编写一个 Python 程序，要求用户输入一句话，然后输出这句话的字符总数（包括空格和标点符号）。
word = input('请输入一句话:')
print(f'字符总数: {len(word)}')

#5.编写一个程序，让用户输入自己的名字、年龄和成绩，然后使用 f-string、format() 和 % 三种方式分别输出以下格式：
name = input('请输入姓名:') 
age = input('请输入年龄: ')
score = input('请输入成绩: ')
print(f'{name}，年龄 {age}，成绩 {score}')
print('{}，年龄 {}，成绩 {}'.format(name, age, score)) # 改进 成绩 {:.2f}
print('%s，年龄 %d，成绩 %f' % (name, int(age), float(score))) # 改进：成绩 %.2f








