"""
Повернуть матрицу на 90 градусов
"""


n = int(input())
matrix = []
for i in range(n):
    row = [x for x in input().split()]
    matrix.append(row)

matrix.reverse()

for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()
