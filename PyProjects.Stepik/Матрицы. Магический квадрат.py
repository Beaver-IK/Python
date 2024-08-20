"""
Магическим квадратом порядка nn называется квадратная таблица размера n×n,
составленная из всех чисел 1, 2, 3, ... n ** 2 так, что суммы по каждому столбцу,
каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
которая проверяет, является ли заданная квадратная матрица магическим квадратом.
"""

def is_sqrt(matrix):
    a = len(matrix) ** 2
    list_digit = [int(x) for x in range(1, a + 1)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] in list_digit:
                list_digit.remove(matrix[i][j])
    if len(list_digit) == 0:
        return True
    else:
        return False

def is_i(matrix):
    a = sum(matrix[0])
    flag = True
    for i in matrix:
      if sum(i) != a:
        flag = False
    return flag

def is_j(matrix):
    flag = True
    a = 0
    for i in range(1):
        for j in range(len(matrix)):
            a += matrix[j][i]
    for i in range(len(matrix)):
        total = 0
        for j in range(len(matrix)):
            total += matrix[j][i]
        if total != a:
            flag = False
    return flag

def is_diag(matrix):
    total = 0
    flag = True
    for i in range(len(matrix)):
            total += matrix[i][i]
            total -= matrix[len(matrix) - i - 1][i]
    if total != 0:
        flag = False
    return flag

n = int(input())
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

flag = 'NO'

if is_sqrt(matrix):
    if is_i(matrix):
        if is_j(matrix):
            if is_diag(matrix):
                flag = 'YES'
print(flag)




