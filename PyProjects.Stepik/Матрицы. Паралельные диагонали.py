
n = int(input())
matrix = []
for i in range(n):
    row = [[0] * n for x in range(n)]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        matrix[i][j] = abs(i - j)

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
