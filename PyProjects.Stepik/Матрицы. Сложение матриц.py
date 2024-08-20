"""
Напишите программу для вычисления суммы двух матриц.
"""


size_list = [int(x) for x in input().split()]
n = size_list[0]
m = size_list[1]

total_matrix = [[0] * m for _ in range(n)]
first_matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    first_matrix.append(row)
input()
second_matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    second_matrix.append(row)

for i in range(n):
    for j in range(m):
        total_matrix[i][j] = first_matrix[i][j] + second_matrix[i][j]

for i in range(n):
    for j in range(m):
        print(total_matrix[i][j], end=' ')
    print()
