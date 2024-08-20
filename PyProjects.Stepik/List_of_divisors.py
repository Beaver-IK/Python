'''На вход программе подается натуральное число n.
Напишите программу, которая создает список состоящий из делителей введенного числа.'''

n = int(input())
list_of_divisors = []
div = 1
while div <= n:
    if n % div == 0:
        list_of_divisors.append(div)
    div += 1
print(list_of_divisors)
