'''На вход программе подается натуральное число nn, а затем n строк.
 Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.'''


main_list = []
for i in range(int(input())):
    line = input()
    if line in main_list:
        continue
    else:
        main_list.append(line)
print(*main_list, sep='\n')
