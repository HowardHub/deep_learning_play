
"""
集合遍历：  for char in words:
集合推导式：char for char in words if words.count(char) == 1，
集合推导式（set comprehension）来创建一个新的集合 uniques_char = {集合推导式}
"""


"""
1. 创建集合并基本操作
	•	创建一个包含 5 个水果名称的集合 fruits = {"苹果", "香蕉", "橙子", "葡萄", "西瓜"}。
	•	向集合中添加一个新水果 "芒果"。
	•	删除 "橙子"（如果存在）。
	•	打印最终的集合。
"""
fruits = {"苹果", "香蕉", "橙子", "葡萄", "西瓜"}
fruits.add('芒果')
fruits.remove('橙子') #改进如果 "橙子" 不在集合中，.remove() 会抛出 KeyError。用fruits.discard('橙子')
fruits.remove('橙子')
print(fruits)



"""
2. 集合去重
	•	让用户输入一串用空格分隔的数字，例如 "1 2 3 4 5 1 2 3 6 7"。
	•	将这些数字存入一个集合，实现 去重。
	•	输出去重后的结果。
"""
numbers = input('请输入一串数字，并用空格分隔')
num_set = set(numbers.split()) #改进：input().split() 返回字符串列表，集合中元素仍然是字符串，而不是数字。
num_set = set(map(int, numbers.split()))
print(num_set)



"""
3. 计算交集、并集、差集
	•	创建两个集合：
    •	计算 交集（即两个集合共有的水果）。
	•	计算 并集（合并所有水果）。
	•	计算 set1 相对于 set2 的 差集（即 set1 有但 set2 没有的元素）。
"""
set1 = {"苹果", "香蕉", "橙子", "葡萄"}
set2 = {"香蕉", "橙子", "梨", "桃子"}
print(f'两个集合的交集：{set1 & set2}')
print(f'两个集合的并集：{set1 | set2}')
print(f'set1 相对于 set2 的 差集是：{set1 - set2}')







"""
4. 判断集合关系
	•	给定两个集合：
    •	判断 B 是否是 A 的子集。
	•	判断 A 是否是 B 的超集。
	•	判断 A 和 B 是否有交集。
"""
A = {1, 2, 3, 4, 5}
B = {2, 3, 4}
print(B.issubset(A))
print(A.issuperset(B))
print(A.isdisjoint(B)) # disjoint为不相交




"""
5. 统计唯一字符
	•	让用户输入一个字符串，例如 "hello world"。
	•	使用集合找出字符串中出现的 唯一字符，并输出结果。
"""
words = input('请输入字符串：')
lst = list(words)
set1 = set() # 总的集合
set_dup = set() # 重复的集合
for word in lst:
    if not (word in set1):
        set1.add(word)
    else:
        set_dup.add(word)

print(f'出现一次的字符：{set1 - set_dup}')


#优化后的代码，unique_chars = {char for char in words if words.count(char) == 1}
# #优化后 使用集合推导式 {char for char in words if words.count(char) == 1}，避免额外存储
# words = input('请输入字符串：')
# unique_chars = {char for char in words if words.count(char) == 1}
# print(f'出现一次的字符：{unique_chars}')




"""
6. 找出两个列表中的相同元素
	•	给定两个列表：
    •	找出两个列表中相同的元素（即 交集）。
	•	找出两个列表中不同的元素（即 对称差集）。
"""
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [5, 6, 7, 8, 9, 10]
set1 = set(list1)
set2 = set(list2)
print(f'两个集合中相同的元素：{set1 & set2}')
print(f'两个集合的对称差{set1 ^ set2}')
print(f'两个集合的对称差{set1.symmetric_difference(set2)}')








"""
7. 计算两组学生的共同爱好
	•	创建两个集合：
    •	找出两组学生 共同喜欢 的运动。
	•	找出两组学生 各自独有 的运动。
"""
group_A = {"篮球", "足球", "乒乓球", "游泳"}
group_B = {"足球", "羽毛球", "游泳", "网球"}
print(f'共同喜欢的运动：{group_A & group_B}')
print(f'A组独有的运动{group_A - group_B}')
print(f'B组独有的运动{group_B - group_A}')



"""
8. 词频统计（去重）
	•	让用户输入一段文本。
	•	按 单词 分割，去重后输出 所有不同的单词。
"""
words = input('请输入一段话')
words = set(words.split())
print(f'去重后的单词：{words}')



"""
9. 两个集合是否相等
	•	给定两个集合：
    •	判断 set1 和 set2 是否相等（即是否包含相同元素）。

"""
set1 = {1, 2, 3, 4, 5}
set2 = {5, 4, 3, 2, 1}
print(set1.issubset(set2) and set2.issubset(set1))
# 优化直接使用 == 进行判断：
print(set1 == set2)
