


strings = ["1", "2", "three", "4", "five"]
processed = [int(s) if s.isdigit() else s for s in strings]
print(processed)  # 输出: [1, 2, 'three', 4, 'five']







matrix =[]
for j in range(3):
    row =[]
    for i in range(3):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)
print(matrix)
