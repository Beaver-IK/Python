"""
Написать программу, принимающую на вход координаты коня, в формате буква+цифра
"""


position = list(input())
y = 'abcdefgh'.find(position[0])
x = int(position[1])
x *= -1
n = 8
matrix = []
for i in range(n):
    row = ['.' for x in range(n)]
    matrix.append(row)

matrix[x][y] = 'N'

for i in range(-8, 0, 1):
    for j in range(n):
        if (i == x + 2) or (i == x - 2):
            if (j == y + 1) or (j == y - 1):
                matrix[i][j] = '*'
        elif (j == y - 2) or (j == y + 2):
            if (i == x + 1) or (i == x - 1):
                matrix[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
