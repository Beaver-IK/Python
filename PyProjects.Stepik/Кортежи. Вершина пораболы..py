"""
Уравнение параболы имеет вид y = ax ** 2 + bx + c, где a != 0.
Напишите программу, которая по введенным значениям a, b, c определяет и выводит вершину параболы.
"""

def pick(a, b, c):

    x = (-b) / (2 * a)
    y = (4 * a * c - b ** 2) / (4 * a)
    return x, y

a = int(input())
b = int(input())
c = int(input())
x, y = pick(a, b, c)
cord_pick = (x, y)
print(cord_pick)
