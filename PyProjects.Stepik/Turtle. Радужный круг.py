import turtle
turtle.Screen().colormode(255)
turtle.Screen().setup(2050, 2050)

colors = [255, 0, 0]
r = 1020
turtle.penup()
turtle.goto(0, -r)

for _ in range(1020):
    turtle.fillcolor(colors[0], colors[1], colors[2])
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.goto(0, -r + 1)
    r -= 1
    if colors[0] == 255 and colors[1] != 255:
        colors[1] += 1
    elif colors[1] == 255 and colors[0] != 0:
        colors[0] -= 1
    elif colors[0] == 0 and colors[1] == 255 and colors[]:
        colors[2] += 1


turtle.done()
