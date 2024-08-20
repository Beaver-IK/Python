"""
На вход программе подается натуральное число n.
Напишите программу, которая выводит первые nn строк треугольника Паскаля.
"""


def pascal(num):
    p = []
    for i in range(num + 1):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = p[i - 1][j - 1] + p[i - 1][j]
        p.append(row)
    return p


n = int(input())
tri_p = pascal(n - 1)
for x in tri_p:
    print(*x)
