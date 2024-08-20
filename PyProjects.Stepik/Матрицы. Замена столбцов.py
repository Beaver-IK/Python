n = int(input())
m = int(input())
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

indexes = [int(x) for x in input().split()]
x = indexes[0]
y = indexes[1]

for e in matrix:
    e[x], e[y] = e[y], e[x]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
