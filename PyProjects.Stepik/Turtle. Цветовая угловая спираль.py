import turtle
from random import choice
color = ('red', 'blue', 'yellow', 'green', 'purple', 'orange')
size = 1
lenght = 20
turtle.left(60)
for _ in range(6):
    for i in range(6):
        turtle.color(choice(color))
        turtle.pensize(size)
        turtle.forward(lenght)
        turtle.left(60)
        size += 0.2
        lenght += 2

turtle.done()
