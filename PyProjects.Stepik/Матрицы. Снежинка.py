


n = int(input())
matrix = [['.'] * n for i in range(n)]
a = n // 2

for i in range(n):
    for j in range(n):
        if i == a or j == a:
            matrix[i][j] = '*'
        if i == j or n == i + j + 1:
            matrix[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
