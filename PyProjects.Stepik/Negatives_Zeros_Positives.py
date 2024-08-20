'''На вход программе подается натуральное число n, а затем n целых чисел.
Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа,
каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.'''

digit_list = []
for digits in range(int(input())):
    digit_list.append(int(input()))
for i in digit_list:
    if i < 0:
        print(i)
for i in digit_list:
    if i == 0:
        print(i)
for i in digit_list:
    if i > 0:
        print(i)

