
import os
import json


"""
📌 题目 1：文件写入
	1.	创建一个名为 test.txt 的文件，并写入 "Hello, Python 文件操作！"。
	2.	关闭文件后，重新打开它，并读取内容，打印到控制台。
"""
with open('test.txt', 'w') as f:
    f.write('Hello, Python 文件操作！')


with open('test.txt', 'r') as f:
    print(f.read())
	
    
# 优化建议：📌 1. 读取文件内容后，应该换行
#•	在 print(f.read()) 时，如果文件末尾没有换行符，打印的内容可能会与下一行 print 输出连在一起，建议使用 print(f.read(), end="")。


"""
📌 题目 2：追加写入
	1.	打开 test.txt 文件，在文件末尾 追加 "这是追加的一行。"。
	2.	关闭文件后，重新读取文件内容，打印到控制台。
"""
# a 以追加模式打开文件（如果文件不存在则创建）
with open('test.txt', 'a') as f:
    f.write('\n这是追加的一行。')
# 优化建议：不断追加内容时，始终保证新的一行在前面，可读性更好。
#   f.write('这是追加的一行。\n')

with open('test.txt', 'r') as f:
    print(f.read())
	
	

"""
📌 题目 3：逐行读取
	1.	创建一个新文件 data.txt，写入以下多行内容：
        第一行数据
        第二行数据
        第三行数据
    2.	读取 data.txt 的所有行，并使用 for 循环逐行打印。
"""
with open('data.txt', 'w') as f:
    f.write('第一行数据')
    f.write('\n第二行数据')
    f.write('\n第三行数据')

with open('data.txt', 'r') as f:
    for line in f.readlines():
        print(line, end="")


"""
📌 题目 4：使用 with open() 处理文件
	1.	使用 with open() 方式打开 test.txt，读取文件内容并打印。
	2.	解释为什么 with open() 方式更推荐。
"""
with open('test.txt', 'r') as f:
    for line in f.readlines():
        print(line, end='')




"""
📌 题目 5：判断文件是否存在
	1.	导入 os 模块，检查 test.txt 是否存在：
	•	如果存在，读取文件内容并打印；
	•	如果不存在，输出 "文件不存在"。
"""
dirs = os.listdir()
file_name = 'test.txt'
if file_name in dirs:
    with open(file_name, 'r') as f:
        for line in f.readlines():
            print(line, end='')
else:
    print('文件不存在')
    
#优化建议：直接用 os.path.exists()，避免 os.listdir() 读取整个目录列表。
if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        for line in f.readlines():
            print(line, end='')
else:
    print('文件不存在')


"""
📌 题目 6：复制文件
	1.	读取 test.txt 文件的内容，并将其复制到新文件 copy_test.txt 中。
	2.	确保 copy_test.txt 也能正确读取内容。
"""
with open('test.txt', 'rb') as src, open('copy_test.txt', 'wb') as dst:
    dst.write(src.read())

with open('copy_test.txt', 'r') as f:
    for line in f.readlines():
        print(line, end='')

#优化建议：如果文件很大，src.read() 可能会消耗大量内存，建议 使用循环逐块读取
with open('test.txt', 'rb') as src, open('copy_test.txt', 'wb') as dst:
    while chunk := src.read(4096):  # 逐块读取 4KB
        dst.write(chunk)




"""
📌 题目 7：统计文件中的单词数
	1.	创建 words.txt，写入 "Python 文件操作是很重要的技能"。
	2.	读取 words.txt 的内容，并统计其中 单词的数量（按空格拆分）。
"""
with open('words.txt', 'w') as f:
    f.write('Python 文件操作是很重要的技能')

with open('words.txt', 'r') as f:
    line = f.readline()
    word_stat = {}
    for word in line.split():
        word_stat[word] = word_stat.get(word, 0) + 1
    print(word_stat)
# 理解有误，题目是统计总单词数，而不是每个单词出现的次数。
with open('words.txt', 'r') as f:
    words = f.read().split()
    print(len(words))
    



"""
📌 题目 8：删除文件
	1.	导入 os 模块，判断 delete_me.txt 是否存在：
	•	如果存在，删除该文件；
	•	如果不存在，输出 "文件不存在"。
"""
dirs = os.listdir()
file_name = 'delete_me.txt'
# 优化：判断存在直接用
if os.path.exists(file_name):
    print('文件存在')
if file_name in dirs:
    print('文件存在')
    os.remove(file_name)
else:
    print('文件不存在')





"""
📌 题目 9：文件异常处理
	1.	尝试读取 non_existent.txt 文件：
	•	如果文件不存在，捕获 FileNotFoundError 并打印 "文件未找到"。
	•	否则，正常读取并打印内容。
"""
try:
    with open('non_existent.txt', 'r') as f:
        for line in f.readlines():
            print(line, end='')
except FileNotFoundError:
    print('文件未找到')
except IOError:
    print('文件读取失败')


"""
📌 题目 10：JSON 文件读写
	1.	创建一个字典：
    2.	将其存入 student.json 文件（JSON 格式）。
	3.	读取 student.json 文件，并解析成 Python 字典，打印出来。

"""
student = {"name": "张三", "age": 20, "city": "北京"}
with open('student.json', 'w') as f:
    #f.write(json.dumps(student))
    json.dump(student, f) #直接使用dump，
    
with open('student.json', 'r') as f:
    #student_dict = json.loads(f.read())
    student_dict = json.load(f) #更直观，也避免 f.read() 额外的步骤
    print(student_dict)

"""
使用场景
	使用 json.dump() 当：
		需要直接将数据写入文件
		处理大型数据，避免内存中保存整个JSON字符串
	使用 json.dumps() 当：
		需要JSON字符串用于网络传输(如API响应)
		需要将JSON数据存储在数据库中
		需要在程序内部处理JSON字符串
"""
