'''
Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы,
главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника,
нумерация начинается с единицы
'''

lines = [input() for x in range(int(input()))]
anton = ['a', 'n', 't', 'o', 'n']
indexes = []
for i in range(len(lines)):
    count = 0
    for j in anton:
        if j in lines[i]:
            a = lines[i].find(j)
            lines[i] = lines[i][a:]
            count += 1
        if count == 5:
            indexes.append(i + 1)
print(*indexes)






