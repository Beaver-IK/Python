"""
Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) целые числа
от 1 до 75 (включительно), при этом центральная клетка является пустой (она заполняется числом 0).
"""
from random import randint, choice

def get_ticket():
    ticket_digits = set()
    while len(ticket_digits) != 24:
        digit = randint(1, 75)
        ticket_digits.add(str(digit))
    ticket_digits = list(ticket_digits)

    ticket = []
    for i in range(5):
        row = []
        for j in range(5):
            if i == j == 2:
                row.append('0')
            else:
                digit = choice(ticket_digits)
                row.append(digit)
                ticket_digits.remove(digit)
        ticket.append(row)

    return ticket

tiket = get_ticket()

for i in range(5):
    for j in range(5):
        print(tiket[i][j].ljust(3), end='')
    print()
