"""
Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы,
стоящие на главной и побочной диагонали, при этом каждый элемент должен остаться в
том же столбце (то есть в каждом столбце нужно поменять местами элемент на главной
диагонали и на побочной диагонали).
"""


n = int(input())
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for i in range(n):
    matrix[i][i], matrix[n-i-1][i] = matrix[n-i-1][i], matrix[i][i]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
