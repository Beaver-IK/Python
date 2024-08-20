import turtle
from random import randrange

turtle.Screen().colormode(255)
turtle.Screen().setup(500, 500)
turtle.penup()
turtle.hideturtle()
turtle.Screen().bgcolor(0, 0, 0)
turtle.speed(0)


def color():
    return randrange(255), randrange(255), randrange(255)

def pos():
    return randrange(-250, 250), randrange(-250, 250)

def star():
    size = randrange(10, 20)
    turtle.fillcolor(color())
    turtle.goto(pos())
    turtle.left(randrange(360))
    turtle.begin_fill()
    for _ in range(5):
        turtle.penup()
        turtle.right(144)
        turtle.forward(size)
    turtle.end_fill()

for _ in range(50):
    star()

turtle.done()
