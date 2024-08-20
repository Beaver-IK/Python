"""
Напишите программу, которая случайным образом назначает каждому ученику его
тайного друга, который будет вместе с ним решать задачи по программированию.

Формат входных данных
На вход программе в первой строке подается число n – общее количество учеников.
Далее идут n строк, содержащих имена и фамилии учеников.
"""


import random

students = [input() for _ in range(int(input()))]

shaffle_students = students[::]

flag = True
while flag:
    for i in range(len(students)):
        if students[i] == shaffle_students[i]:
            random.shuffle(shaffle_students)
            flag = True
            break
        else:
            flag = False

match = dict(zip(students, shaffle_students))
shaffle_students.clear()
students.clear()

for key in match:
    print(f'{key} - {match[key]}')
