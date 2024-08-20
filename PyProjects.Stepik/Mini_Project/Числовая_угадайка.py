'''Описание проекта: программа генерирует случайное число в диапазоне от 11 до 100100 и просит
пользователя угадать это число. Если догадка пользователя больше случайного числа,
то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'.
Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.'''


from random import *

def is_valid(digit):
    flag = False
    if 1 <= digit <= 100:
        flag = True
    return (flag)

num = randint(1,100)
print('Добро пожаловать в числовую угадайку')

count = 0
while True:
    n = int(input())
    count += 1
    if is_valid(n):
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        elif n == num:
            print('Вы угадали, поздравляем!')
            q = input('Хотит сыграть еще? д = да, н = нет')
            if q == 'д':
                num = randint(1,100)
                continue
            else:
                break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
print('Число попыток:', count)

