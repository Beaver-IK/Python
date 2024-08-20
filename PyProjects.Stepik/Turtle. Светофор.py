import turtle

turtle.speed(0) #устнавливаем черепашку, чтоб светофор был в центре
turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.backward(25)
turtle.pendown()

turtle.fillcolor('black') # Рисуем корпус светофора
turtle.begin_fill()
for _ in range(2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
turtle.end_fill()

colors = ('green', 'yellow', 'red') # Кортеж с цветами светофора
a = 30 # Радиус сигнала светофора
b = 100 - (4 * a / 3) # отступ между каждым сигналом
turtle.penup()
turtle.forward(50)
turtle.left(90)
turtle.forward(a)
for color in colors: # Рисуем сигналы светофора
    turtle.pendown()
    turtle.right(90)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(a)
    turtle.end_fill()
    turtle.left(90)
    turtle.penup()
    turtle.forward(b + a)



turtle.done()
