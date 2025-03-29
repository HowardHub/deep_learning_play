

"""
    1.编写一个 Python 程序，让用户输入一个数字，并判断：
	•	大于 0 → 输出 "这个数是正数"
	•	等于 0 → 输出 "这个数是零"
	•	小于 0 → 输出 "这个数是负数"
"""
num = input("请输入数字")
try:
    num = float(num)
    if num > 0:
        print('这个数是正数')
    elif num == 0:
        print('这个数是零')
    else:
        print('这个数是负数')
except ValueError:
    print('输入的不是数字')


"""
2.让用户输入一个 0-100 之间的成绩，然后按照以下规则输出评级：
	•	90-100: "优秀"
	•	80-89: "良好"
	•	70-79: "中等"
	•	60-69: "及格"
	•	0-59: "不及格"
"""
num = input("请输入成绩")
try:
    num = float(num)
    if num > 100:
        print('成绩不能超过100')
    elif num >= 90 and num <= 100:
        print('优秀')
    elif num >= 80 and num <= 89:
        print('良好')
    elif num >= 70 and num <= 79:
        print('中等')
    elif num >= 60 and num <= 69:
        print('及格')
    elif num >= 0 and num <= 59:
        print('不及格')
    else:
        print('成绩不能小于0')
except ValueError:
    print('输入的不是数字')


"""
    3.用户输入一个年份，判断它是否是闰年。
    闰年的判断规则：
	•	能被 4 整除但不能被 100 整除，或者
	•	能被 400 整除
"""
years = input("请输入年份")
try:
    years = float(years)
    if (years % 4 == 0 and years % 100 > 0) or years % 400 == 0:
        #print(f'{years} 是闰年')
        print('{:.0f}是闰年'.format(years))
    else:
        print('{:.0f}不是闰年'.format(years))

except ValueError:
    print('输入的不是数字')




"""
    4.题目：
    假设出租车的计价规则如下：
	•	3 公里以内起步价：12 元
	•	超过 3 公里但不超过 10 公里：每公里 2.5 元
	•	超过 10 公里：每公里 3.5 元

    请编写程序，让用户输入行驶的公里数，然后计算总费用。
"""
# 采用阶梯式价格！
kms = input("请输入行驶的公里数: ")
try:
    kms = float(kms)
    total_fee = 0
    if kms < 0:
        print('输入的公里数不合法')
    elif kms <= 3:
        total_fee = 12
    elif kms > 3 and kms < 10:
        total_fee = 12 + kms * 2.5
    else:
        total_fee = 12 + kms * 3.5
    
    print('您的打车费用是: {:.2f} 元'.format(total_fee))
except ValueError:
    print('你的输入不合法')


"""
    5.编写一个 ATM 取款机程序：
	•	账户余额 balance = 1000
	•	让用户输入取款金额
	•	如果金额大于余额，输出 "余额不足"
	•	如果金额小于等于余额且是 100 的倍数，扣除金额并显示剩余余额
	•	如果金额不是 100 的倍数，提示 "请输入 100 的整数倍"
"""

count = input('请输入取款金额: ')
try:
    balance = 1000
    count = float(count)
    if count > balance:
        print('余额不足')
    else:
        if count % 100 == 0:
            print('取款成功，您的余额是 {:.0f} 元'.format(balance - count))
        else:
            print('请输入 100 的整数倍')
except ValueError:
    print('你的输入非法')




# GPT建议
"""
    1.	使用 except ValueError: 代替 except:
	2.	避免 try-except 包裹整个 if 逻辑
	3.	用 int() 代替 float() 处理年份、取款金额
	4.	出租车费用计算修正
	5.	ATM 机增加负数输入检查
"""