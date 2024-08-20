import turtle

turtle.penup()
turtle.speed(1000)
turtle.shape('turtle')
lenght = 1
turn = 24
for _ in range(5):
    for _ in range(15):
        turtle.forward(lenght)
        turtle.right(turn)
        turtle.stamp()
        lenght += 0.5
