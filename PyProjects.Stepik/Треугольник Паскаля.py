"""
На вход программе подается число n.
Напишите программу, которая возвращает указанную строку
треугольника Паскаля в виде списка (нумерация строк начинается с нуля).
"""


def pascal(num):
    p = []
    for i in range(num + 1):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = p[i - 1][j - 1] + p[i - 1][j]
        p.append(row)
    return p[-1]


n = int(input())
for x in range(n + 1):
    print(*pascal(x))
