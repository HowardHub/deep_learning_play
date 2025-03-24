import numpy as np



x = np.array([1, 2, 3])
print(x)



y = np.array([2,3,5])

print(x+y)
print(x-y)
print(x*y)
print(x/y)


A = np.array([[1,2], [3, 4]])
print(A)
print(A.shape)

# 广播
print('广播')
print(A * 10)



# 访问元素
print('访问元素')
B = np.array([[11, 40], [12, 30], [9, 21]])
for i in B:
    print(i)

for i in B:
    for j in i:
        print(j)

print(B[0])
print(B[1][1])
