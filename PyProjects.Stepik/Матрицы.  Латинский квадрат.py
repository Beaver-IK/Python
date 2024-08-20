"""
Латинским квадратом порядка n называется квадратная матрица размером n×n,
каждая строка и каждый столбец которой содержат все числа от 1 до n.
Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.
"""


n = int(input())
first_matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    first_matrix.append(row)

first_matrix.reverse()

second_matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        second_matrix[i][j] = first_matrix[j][i]

flag1 = True

for i in range(n):
    for j in range(n):
        if first_matrix[i].count(j + 1) != 1 and second_matrix[i].count(j + 1) != 1:
            flag1 = False
        if sum(first_matrix[i]) != sum(second_matrix[j]):
                flag1 = False


if flag1:
    flag2 = True
    for i in range(n):
        first_matrix[i].sort()
        second_matrix[i].sort()

    for i in range(n):
        for j in range(n):
            if first_matrix[i][j] != second_matrix[i][j]:
                flag2 = False
        if flag2 == False:
            break

    if flag2:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
