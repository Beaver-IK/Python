'''
На вход программе подается строка текста.
Напишите программу, которая определяет является ли введенная строка корректным телефонным номером.
Строка текста является корректным телефонным номером если она имеет формат:
abc-def-hijk или
7-abc-def-hijk
где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9
'''


phone_num = input()
if len(phone_num) == 11 or len(phone_num) == 14:
    phone_num = phone_num.replace('-','')
    if phone_num.isdigit():
        if len(phone_num) == 11 and phone_num[0] == '7':
            print('YES')
        elif len(phone_num) == 10:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
