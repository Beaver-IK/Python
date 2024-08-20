'''На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.
Напишите программу, которая определяет является ли введенная строка текста корректным ip-адресом.'''


line = input()
ip = line.split('.')
flag = False
if len(ip) == 4:
    for i in ip:
        if 0 <= int(i) <= 255:
            flag = True
        else:
            flag = False
            break
else:
    flag = False
if flag == True:
    print('YES')
else:
    print('NO')

