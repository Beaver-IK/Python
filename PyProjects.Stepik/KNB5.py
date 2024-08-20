'''
Камень, ножницы, бумага в пять вариантов
'''

def knb(t, r):
    options = ['камень', 'бумага', 'ножницы', 'Спок', 'ящерица']
    a = options.index(t)
    b = options.index(r)
    if a - b == 0:
        print('')
    elif a - b in [2, 4, -1, -3]:
        print('Руслан')
    else:
        print('Тимур')
a = input()
b = input()
knb(a, b)
