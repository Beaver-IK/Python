import turtle
n = int(input())
m = 360 / n

turtle.dot(10)
for _ in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.left(m)

r = 10
for _ in range(9):
    turtle.left(90)
    turtle.penup()
    turtle.backward(10)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(r)
    r += 10

turtle.done()
