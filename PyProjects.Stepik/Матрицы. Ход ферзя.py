"""
Ходы ферзя
"""


position = list(input())
y = 'abcdefgh'.find(position[0])
x = '87654321'.find(position[1])
n = 8
matrix = []
for i in range(n):
    row = ['.' for x in range(n)]
    matrix.append(row)


for i in range(n):
    for j in range(n):
        if j == y:
            matrix[-i][j] = '*'
        if i == x:
            matrix[i][j] = '*'
        if x - i == y - j or i + j + 1 == x + y + 1:
            matrix[i][j] = '*'

matrix[x][y] = 'Q'


for i in range(n): #Печатаем матрицу
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
