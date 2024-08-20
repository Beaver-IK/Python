"""
На вход программе подаются два натуральных числа nn и mm — количество строк
и столбцов в матрице, затем nn строк по mm целых чисел в каждой, отделенных символом пробела.

Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.
"""


n = int(input())
m = int(input())
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

max_digit = matrix[0][0]

option = 1
flag = False
while option < 3:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_digit and option == 1:
                max_digit = matrix[i][j]
            if matrix[i][j] == max_digit and option == 2:
                print(i, j)
                flag = True
                break
        if flag:
            break
    option += 1
