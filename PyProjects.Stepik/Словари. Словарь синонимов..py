"""
Вам дан словарь, состоящий из пар слов-синонимов.
Повторяющихся слов в словаре нет. Напишите программу,
которая для одного данного слова определяет его синоним.
"""


list_dict = []
for _ in range(int(input())):
    dict_tuple = input().split()
    dict_tuple = tuple(dict_tuple)
    list_dict.append(dict_tuple)

sin_dict = {}
for elem in list_dict:
    sin_dict[elem[0]] = elem[1]

request = input()

for key in sin_dict:
    if request in sin_dict and request == key:
        print(sin_dict[key])
    elif sin_dict[key] == request:
        print(key)
