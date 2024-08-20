list_size = [int(x) for x in input().split()]
n = list_size[0]
m = list_size[1]
matrix = []
for i in range(n):
    row = [int(0) * m for j in range(m)]
    matrix.append(row)

count = 0
for a in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == a:
                count += 1
                matrix[i][j] = count
                break

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
