'''
Напишите функцию convert_to_python_case(text), которая принимает
в качестве аргумента строку в «верблюжьем регистре»
и преобразует его в «змеиный регистр».
'''


def convert_to_python_case(text):
    list_line = list(text)
    python_list = [list_line[0]]
    for i in range(1, len(list_line)):
        if list_line[i].isupper():
            python_list.append('_')
            python_list.append(list_line[i])
        else:python_list.append(list_line[i])
    return (''.join(python_list).lower())

txt = input()
print(convert_to_python_case(txt))
