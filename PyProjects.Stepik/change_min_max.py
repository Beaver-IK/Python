'''На вход программе подается строка текста, содержащая различные натуральные числа.
Из данной строки формируется список чисел. Напишите программу, которая меняет местами
минимальный и максимальный элемент этого списка.'''

digit_list = input().split()
mini_index = digit_list.index(min(digit_list, key=int))
maxi_index = digit_list.index(max(digit_list, key=int))
digit_list[maxi_index], digit_list[mini_index] = digit_list[mini_index], digit_list[maxi_index]
print(*digit_list)
