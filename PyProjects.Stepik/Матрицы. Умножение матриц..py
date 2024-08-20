"""
Напишите программу, которая перемножает две матрицы.
"""


def valid_size(a, d):
    if a == d:
        return True
    else:
        return False


size_list_1 = [int(x) for x in input().split()]
n1 = size_list_1[0]
m1 = size_list_1[1]
first_matrix = []
for i in range(n1):
    row = [int(x) for x in input().split()]
    first_matrix.append(row)

input()

size_list_2 = [int(x) for x in input().split()]
n2 = size_list_2[0]
m2 = size_list_2[1]
second_matrix = []
for i in range(n2):
    row = [int(x) for x in input().split()]
    second_matrix.append(row)

if valid_size(n1, m2):
    mul_matrix = [[0] * n1 for _ in range(m2)]

    for i in range(n1):
        for j in range(m2):
            row = []
            for k in range(n2):
                a = first_matrix[i][k] * second_matrix[k][j]
                row.append(a)
            mul_matrix[i][j] = sum(row)

    for i in range(n1):
        for j in range(m2):
            print(mul_matrix[i][j], end=' ')
        print()


else:
    print("""Для умножения матриц, требуется сответствие количества столбцов в первой матрице,
количеству строк во второй матрице.""")
