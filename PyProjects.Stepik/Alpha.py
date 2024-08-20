'''Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]'''


l_ist = []
mul = 0
for i in range(97, 97 + 26):
    char = chr(i)
    mul += 1
    l_ist.append(char * mul)
print(l_ist)
