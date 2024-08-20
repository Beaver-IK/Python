"""
На вход программе подаются два предложения. Напишите программу, которая определяет,
являются они анаграммами или нет.
Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.
"""


a = tuple(input().lower())
b = tuple(input().lower())


a_1 = {}
b_1 = {}

for key in a:
    if key not in '.,!?:;- ':
        a_1[key] = a_1.get(key, 0) +1

for key in b:
    if key not in '.,!?:;- ':
        b_1[key] = b_1.get(key, 0) +1


flag = True
for key in a_1:
    if key not in b_1 or a_1[key] != b_1[key]:
        flag = False

if flag:
    print('YES')
else:
    print('NO')
