"""
Возвести матрицу в степень
"""


n = int(input())
first_matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    first_matrix.append(row)

second_matrix = [row[:] for row in first_matrix]
'''for i in range(n):
    row = []
    for j in range(n):
        row.append(first_matrix[i][j])
    second_matrix.append(row)
'''
stp = int(input())

for l in range(stp - 1):
    mul_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            row = []
            for k in range(n):
                a = second_matrix[i][k] * first_matrix[k][j]
                row.append(a)
            mul_matrix[i][j] += sum(row)
    first_matrix = mul_matrix


for i in range(n):
    for j in range(n):
        print(first_matrix[i][j], end=' ')
    print()
print()
