import turtle
turtle.speed(5)

colors = ('blue', 'black', 'red', 'yellow', 'green')

r = 90

turtle.penup()
turtle.pensize(10)
turtle.goto(85.00, -120.00)
turtle.color(colors[-1])
turtle.pendown()
turtle.circle(r)
turtle.penup()
turtle.goto(0, 0)
turtle.backward(200)
for c in range(4):
    turtle.pendown()
    turtle.color(colors[c])
    turtle.circle(r)
    turtle.penup()
    turtle.forward(190)
    if c == 2:
        turtle.goto(-105, -120)

print(turtle.pos())
turtle.done()
