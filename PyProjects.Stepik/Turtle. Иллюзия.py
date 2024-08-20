import turtle
from math import sqrt as S


turtle.pensize(4) # Устанавливаем значение пера

a = 300 # сторона треугольника
h = a * S(3) / 2 # Высота треугольника
turtle.penup()
turtle.goto(-150.00, -86.60) # Устанавливаем черепашку так, чтоб рисунок оказался в центре холста
for _ in range(3): # Рисуем первый треугольник
    turtle.pendown()
    turtle.forward(a)
    turtle.left(120)
    turtle.penup()

turtle.left(90) # перемещаем черепашку, для рисования второго треугольника
turtle.forward(h / 3 * 2)
turtle.right(90)

for _ in range(3): # по очертанию второго треугольника, расставляем точки
    turtle.forward(a)
    turtle.dot(100)
    turtle.right(120)

turtle.pencolor('white') # задаем цвет заливки и пера
turtle.fillcolor('white')
turtle.pendown()

turtle.begin_fill() # чертим втором трекгольник и заливаем его
for _ in range(3):
    turtle.forward(a)
    turtle.right(120)
turtle.end_fill()

turtle.done()
