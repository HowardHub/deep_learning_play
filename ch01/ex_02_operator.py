
#1.编写一个程序，让用户输入矩形的长和宽，然后计算并输出：
height = input("请输入矩形的长:")
width = input("请输入矩形的宽:")
if height.isdigit() and width.isdigit():
    height = int(height)
    width = int(width)
    print(f'矩形面积:{height * width}')
    print(f'矩形周长:{2 * (height+width)}')
else:
    print("你输入的数据非法")

# 改进版本
height = input("请输入矩形的长:")
width = input("请输入矩形的宽:")
try:
    height = float(height)
    width = float(width)
    print(f'矩形面积:{height * width}')
    print(f'矩形周长:{2 * (height+width)}')
except:
    print('你的输入有误！')



#2.让用户输入一个两位数（10-99），然后输出：
#•	个位数（使用 % 取余）
#•	十位数（使用 // 整除）
num = input('请输入一个两位数')
if num.isdigit():
    num = int(num)
    if num < 10 or num > 99:
        print('你输入的不是两位数！')
    else:
        print(f'个位数是：{num%10}')
        print(f'十位数是：{num//10}')
else:
    print('你输入的不是数字！')


#3.让用户输入两个数字，并使用比较运算符判断它们是否相等。如果相等，输出 "两个数相等"，否则输出 "两个数不相等"。
# 问题： 你的 if num1 == num2: 只是比较字符串，不会自动转换为数值。
# 比如：输入 "10" 和 "010"，它们是不同的字符串，但数值其实相等！
# 改进点：转换为 float 以确保数值比较，而不是字符串比较。
num1 = input('请输入第一个数字: ')
num2 = input('请输入第二个数字：')
if num1.isdigit() and num2.isdigit():
    if num1 == num2:
        print('两个数相等')
    else:
        print('两个数不相等')
else:
    print('请输入数字')

#4.让用户输入一个年龄，并判断这个人是否是青少年（13~19岁之间）。如果是，输出 "你是青少年"，否则输出 "你不是青少年"。
age = input('请输入年龄')
if age.isdigit():
    age = int(age)
    if age >= 13 and age <= 19:
        print('你是青少年')
    else:
        print('你不是青少年')
else:
    print('你输入的不是数字')


#5.让用户输入一个整数，然后使用位运算符计算它的二进制表示中 1 的个数。
# 提示你可以用 bin(x).count('1') 来计算 1 的个数
num = input('请输入一个整数')
if num.isdigit():
    num = int(num)
    binary_num = bin(num)
    print(f'{num} 的二进制是 {binary_num}，1 的个数是 {binary_num.count("1")}')
else:
    print('你输入的不是整数')
# 🔹 问题： isdigit() 不能识别负数，而 bin(num) 处理负数时会生成前缀 -0b...，导致 count('1') 计算错误。
# 🔹 优化方案： 用 abs(num) 确保 bin() 只对正整数处理。
try:
    num = int(num)
    binary_num = bin(num)
    print(f'{num} 的二进制是 {binary_num}，1 的个数是 {bin(abs(num)).count("1")}')
except:
    print('你的输入有误！')