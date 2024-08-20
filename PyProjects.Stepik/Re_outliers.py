'''На вход программе подается натуральное число nn, а затем nn различных натуральных чисел.
Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел,
а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.'''


'''
digit_list = []
for i in range(int(input())):
    digit_list.append(int(input()))
del digit_list[digit_list.index(min(digit_list))]
del digit_list[digit_list.index(max(digit_list))]
print(*digit_list, sep='\n')
'''
digit_list = []
for i in range(int(input())):
    digit_list.append(int(input()))
digit_list.remove(min(digit_list))
digit_list.remove(max(digit_list))
print(*digit_list, sep='\n')
