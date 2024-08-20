"""
В файловую систему компьютера, на котором развернута наша ❤️
платформа Stepik, проник опасный вирус и сломал контроль прав доступа к файлам.
Говорят, вирус написал один из студентов курса Python для начинающих.

Для каждого файла известно, с какими действиями можно к нему обращаться:

запись W (write, доступ на запись в файл);
чтение R (read, доступ на чтение из файла);
запуск X (execute, запуск на исполнение файла).
Напишите программу для восстановления контроля прав доступа к файлам.
Ваша программа для каждого запроса должна будет возвращать OK если выполняется допустимая
операция, и Access denied, если операция недопустима.
"""

access_rights = {'write': 'W', 'read': 'R','execute': 'X'}

rights_files = {}
for _ in range(int(input())):
    file = tuple(x for x in input().split())
    file_dict = {file[0] : set(file[1:])}
    rights_files.update(file_dict)

for _ in range(int(input())):
    file = [x for x in input().split()]
    file[0] = access_rights[file[0]]
    if file[0] in rights_files[file[1]]:
        print('OK')
    else:
        print('Access denied')
"""
5
my_pycode.exe W X
log_n X W R
ave R
lucky_m W R
dnsss.py W
6
execute ave
read dnsss.py
write log_n
execute log_n
read ave
write my_pycode.exe
"""
