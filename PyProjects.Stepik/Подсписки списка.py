"""
Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько,
и даже ни одного. Например, [1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4].
Список [2, 3] — подсписок списка [1, 2, 3, 4], но список [2, 4] не подсписок списка [1, 2, 3, 4],
так как элементы 2 и 4 во втором списке не смежные. Пустой список — подсписок любого списка.
Сам список — подсписок самого себя, то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].

На вход программе подается строка текста, содержащая символы. Из данной строки формируется список.
Напишите программу, которая выводит список, содержащий все возможные подсписки списка, включая пустой список.
"""




line = [x for x in input().split()]
finish_list = [[]]
shift = 1
while shift <= len(line):
    i = 0
    while i + shift <= len(line):
        finish_list.append(line[i:i + shift])
        i += 1
    shift += 1

print(finish_list)
