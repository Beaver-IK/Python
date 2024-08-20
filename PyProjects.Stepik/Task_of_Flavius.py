'''
n человек, пронумерованных числами от 11 до nn, стоят в кругу.
Они начинают считаться, каждый kk-й по счету человек выбывает из круга,
после чего счет продолжается со следующего за ним человека.
Напишите программу, определяющую номер человека, который останется в кругу последним.
'''

def flavius(num, step):
    digit_list = [x for x in range(1, num + 1)]
    while len(digit_list) != 1:
        for _ in range(step - 1):
            digit_list.append(digit_list[0])
            del digit_list[0]
        del digit_list[0]
    return (digit_list)

n, k = int(input()), int(input())
print(*flavius(n, k))
