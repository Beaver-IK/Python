"""
Напишите программу, которая вычисляет сумму элементов:
верхней четверти; правой четверти; нижней четверти; левой четверти.
"""

n = int(input())
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
up = 0
right = 0
down = 0
left = 0
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            up += matrix[i][j]
        elif i < j and i > n - 1 - j:
            right += matrix[i][j]
        elif i > j and i > n - 1 - j:
            down += matrix[i][j]
        elif i > j and i < n - 1 - j:
            left += matrix[i][j]
print('Верхняя четверть:', up)
print('Правая четверть:', right)
print('Нижняя четверть:', down)
print('Левая четверть:', left)
