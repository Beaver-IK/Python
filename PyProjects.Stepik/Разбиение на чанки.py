"""
На вход программе подаются две строки, на одной символы, на другой число n.
Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число,
задающее размер чанка (куска), а возвращает список из чанков указанной длины.
"""


def chunked(a, b):
    finish_list = []
    i = 0
    while len(a) > b:
        row = []
        for _ in range(b):
            row.append(a.pop(i))
        finish_list.append(row)
    if len(a) < b:
        finish_list.append(a)
    return finish_list


line = input().split()
n = int(input())
print(chunked(line, n))
