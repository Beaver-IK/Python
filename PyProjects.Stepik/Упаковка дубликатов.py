"""
На вход программе подается строка текста, содержащая символы.
Напишите программу, которая упаковывает последовательности одинаковых символов
заданной строки в подсписки.
"""


chr_list = input().split()
hit_list = []
i = 0
while len(chr_list) > 0:
    row = []
    while len(chr_list) > 0:
        if len(row) == 0:
            row.append(chr_list.pop(i))
        elif str(chr_list[i]) == str(row[0]):
            row.append(chr_list.pop(i))
        else:
            break
    hit_list.append(row)
print(hit_list)
