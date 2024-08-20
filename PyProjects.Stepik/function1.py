'''На вход программе подается натуральное число n, а затем n целых чисел.
Напишите программу, которая для каждого введенного числа x выводит значение функции
f(x) = x^2 + 2x + 1 f(x) = x2 + 2x + 1, каждое на отдельной строке.'''


n = int(input())
main_list = []
first_list = []
for i in range(n):
    x = int(input())
    first_list.append(i + 1)
    main_list.append(x ** 2 + 2 * x + 1)
print(*first_list, sep='\n')
print()
print(*main_list, sep='\n')
