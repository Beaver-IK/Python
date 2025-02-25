'''
Арифметической прогрессией называется последовательность чисел a1+a2+a3...an

На вход программе подаются три целых числа: 
a, d и n, каждое на отдельной строке.

Выходные данные
Программа должна вывести 
n-ый член арифметической прогрессии.
'''

a, d, n = int(input()), int(input()), int(input())

def arithmetic_prog(a, d, n):
    return a+d*(n-1)

print(arithmetic_prog(a, d, n))