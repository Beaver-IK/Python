'''На вход программе подается натуральное число n \ge 2n≥2, а затем nn целых чисел.
Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел
(0 и 1, 1 и 2, 2 и 3 и т.д.).'''


n = int(input())
total_list = []
main_list = []
for i in range(n):
    digit = int(input())
    main_list.append(digit)
for j in range(len(main_list) - 1):
    total_list.append(main_list[j] + main_list[j + 1])
print(total_list)
