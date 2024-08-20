"""
Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов,
состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
Формат входных данных
На вход программе подаются два числа n и m, каждое на отдельной строке.

Должна быть проверка на наличие одно буквы в верхнем регистре, в нижнем регистре и цифры.
"""
import random
import string

n = int(input())  # кол-во
m = int(input())  # длина


def generate_pas(length):
    chars = string.ascii_letters + string.digits
    chars = tuple(set(chars) - set('0oOIl1'))
    pass_word = random.sample(chars, length)
    flag = True
    while flag:
        upper_count = 0
        lower_count = 0
        digit_count = 0
        for char in password:
            if str(char).isupper():
                upper_count += 1
            if str(char).islower():
                lower_count += 1
            if str(char).isdigit():
                digit_count += 1
        if upper_count != 0 and lower_count != 0 and digit_count != 0:
            flag = False
        else:
            pass_word = random.sample(chars, length)

    return ''.join(pass_word)


def generate_pass(count, length):
    pass_list = []
    while len(pass_list) != count:
        pass_list.append(generate_pas(length))

    return pass_list


for password in generate_pass(n, m):
    print(password)
