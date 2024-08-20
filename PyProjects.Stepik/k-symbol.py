'''На вход программе подается натуральное число n и n строк, а затем число k.
Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.'''


n = int(input())
main_list = []
for i in range(n):
    line = input()
    main_list.append(line)
k = int(input())
for j in range(len(main_list)):
    if len(main_list[j]) < k:
        continue
    else:
        print(main_list[j][k - 1], end='')
