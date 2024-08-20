"""
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
"""

n = int(input())
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False

if flag:
    print('YES')
else:
    print('NO')
