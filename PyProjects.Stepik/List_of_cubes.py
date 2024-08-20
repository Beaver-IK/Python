'''На вход программе подается натуральное число nn, а затем nn целых чисел.
Напишите программу, которая создает из указанных чисел список их кубов.'''


n = int(input())
l_ist = []
for i in range(n):
    digit = int(input())
    digit **= 3
    l_ist.append(digit)
print(l_ist)
