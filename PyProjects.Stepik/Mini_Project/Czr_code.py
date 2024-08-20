'''
Описание проекта: требуется написать программу, способную шифровать и дешифровать текст
в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:

направление: шифрование или дешифрование;
язык алфавита: русский или английский;
шаг сдвига (со сдвигом вправо).
'''


def engl(a, b, c):
    list_line = list(c)
    new_list = []
    if a == 1:
        for i in list_line:
            sim = ord(i) + b
            if i.isalpha():
                if i.isupper():
                    if sim > 90:
                        sim -= 26
                        sim = chr(sim)
                        new_list.append(sim)
                    else:
                        new_list.append(chr(sim))
                elif sim > 122:
                    sim -= 26
                    sim = chr(sim)
                    new_list.append(sim)
                else:
                    new_list.append(chr(sim))
            else:
                new_list.append(i)
    if a == 0:
        for i in list_line:
            sim = ord(i) - b
            if i.isalpha():
                if i.isupper():
                    if sim < 65:
                        sim += 26
                        sim = chr(sim)
                        new_list.append(sim)
                    else:
                        new_list.append(chr(sim))
                elif sim < 97:
                    sim += 26
                    sim = chr(sim)
                    new_list.append(sim)
                else:
                    new_list.append(chr(sim))
            else:
                new_list.append(i)
    return (''.join(new_list))

def rus(a, b, c):
    list_line = list(c)
    new_list = []
    if a == 1:
        for i in list_line:
            sim = ord(i) + b
            if i.isalpha():
                if i.isupper():
                    if sim > 1071:
                        sim -= 32
                        sim = chr(sim)
                        new_list.append(sim)
                    else:
                        new_list.append(chr(sim))
                elif sim > 1103:
                    sim -= 32
                    sim = chr(sim)
                    new_list.append(sim)
                else:
                    new_list.append(chr(sim))
            else:
                new_list.append(i)
    if a == 0:
        for i in list_line:
            sim = ord(i) - b
            if i.isalpha():
                if i.isupper():
                    if sim < 1040:
                        sim += 32
                        sim = chr(sim)
                        new_list.append(sim)
                    else:
                        new_list.append(chr(sim))
                elif sim < 1072:
                    sim += 32
                    sim = chr(sim)
                    new_list.append(sim)
                else:
                    new_list.append(chr(sim))
            else:
                new_list.append(i)
    return (''.join(new_list))

crypt = int(input('Шифруем или дешифруем? \n (1) - шифруем \n (0) - дешифруем \n'))
lang = int(input('Выберете язык: \n (1) - English \n (2) - Русский \n'))
step = int(input('Обозначте шаг шифрования\n'))
if lang == 1:
    line = input('Please, enter the text: \n')
    print(engl(crypt, step, line))
elif lang == 2:
    line = input('Пожалуйста, введите текст:\n')
    print(rus(crypt, step, line))

