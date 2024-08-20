'''Описание проекта: программа генерирует заданное количество паролей и включает в себя
умную настройку на длину пароля, а также на то, какие символы
требуется в него включить, а какие исключить.'''

import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

def generate_password(lenght, chars):
    pas = random.sample(chars, lenght)
    return (''.join(pas))

n = int(input('Сколько паролей надо сгенерировать?:'))
l = int(input('Сколько символов должно быть в пароле?:'))
dig = input('Включать ли цифры 0123456789? (y/n)')
adc_cap = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abc = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
ch = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
exc = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

if dig == 'y':
    chars += digits
if adc_cap == 'y':
    chars += uppercase_letters
if abc == 'y':
    chars += lowercase_letters
if ch == 'y':
    chars += punctuation
if exc == 'y':
    for c in 'il1Lo0O':
        chars.replace(c,'')
for i in range(n):
    print(generate_password(l, chars))
