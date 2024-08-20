'''
На вход программе подается натуральное число в десятичной системе счисления.
Напишите программу, которая переводит его в двоичную, восьмеричную и шестнадцатеричную системы счисления.
'''

def transform(num):
    a = str(bin(num))
    a = a[2:]
    b = str(oct(num))
    b = b[2:]
    c = str(hex(num))
    c = c[2:].upper()
    return (a, b, c)

n = int(input())
n_bin, n_oct, n_hex = transform(n)
print(n_bin)
print(n_oct)
print(n_hex)
