import turtle as T
import random as R

T.pensize(3)
T.speed(0)
T.hideturtle()
height = 1000
width = 800
T.Screen().setup(height, width)
T.Screen().colormode(255)


def color(): # Функция подбора цвета
    r = R.randint(1, 255)
    g = R.randint(1, 255)
    b = R.randint(1, 255)
    return r, g, b

def pos(size): #Функция установки начальной точки, принимает размер снежинки, чтоб она не выходила за края холста
    x = 0
    y = 0
    while True:
        x = R.randint(-500, 500)
        y = R.randint(-400, 400)
        if abs(x) - size < 0 or abs(x) + size > 500:
            continue
        elif abs(y) - size < 0 or abs(y) + size > 400:
            continue
        else:
            T.penup()
            T.goto(x, y)
            T.pendown()
            break

def snowflake(): # Функия рисования снежинки, принимает размер снежинки
    size = R.randrange(10, 110, 10)
    a = size / 4
    T.pencolor(color())
    pos(size)
    for _ in range(8):
        T.forward(a)
        for _ in range(4):
            T.left(45)
            T.forward(a)
            T.backward(a)
            T.right(90)
            T.forward(a)
            T.backward(a)
            T.left(45)
            T.forward(a)
        T.backward(size + a)
        T.left(45)


for _ in range(20):
    snowflake()

T.done()
