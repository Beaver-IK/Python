import turtle

turtle.Screen().bgcolor('darkblue')

boba = turtle.Turtle()
boba.color('orange')
boba.hideturtle()

biba = turtle.Turtle()
biba.color('darkblue')
biba.hideturtle()
biba.penup()
biba.goto(300, 0)

x = 300
while x > -300:
    turtle.tracer(15, 0)
    boba.dot(300)
    biba.dot(300)
    x -= 1
    biba.goto(x, 0)

turtle.done()
