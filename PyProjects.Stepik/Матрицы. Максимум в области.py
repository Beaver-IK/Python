



n = int(input())
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

max_digit = matrix[0][0]

for i in range(n):
    for j in range(n):
        if n - j - 1 < i or i + j + 1 == n:
            if matrix[i][j] > max_digit:
                max_digit = matrix[i][j]
print(max_digit)
