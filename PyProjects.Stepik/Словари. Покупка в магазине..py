"""
Напишите программу для подсчета количества единиц
каждого вида товара из приобретенных каждым покупателем интернет-магазина.
"""


order = {}
for _ in range(int(input())):
    name = tuple(input().split())
    to_order = {name[0] : {name[1] : int(name[2])}}
    if name[0] in order and name[1] in order[name[0]]:
        order[name[0]][name[1]] += to_order[name[0]][name[1]]
    elif name[0] in order and name[1] not in order[name[0]]:
        order[name[0]][name[1]] = to_order[name[0]][name[1]]
    else:
        order.setdefault(name[0], to_order[name[0]])


for name in sorted(order):
    print(f'{name}:')
    for pos in sorted(order[name]):
        print(f'{pos} {order[name][pos]}')

