from turtle import *

def hexagon(side):
    for _ in range(6):
        forward(side)
        right(60)

for _ in range(6):
    hexagon(100)
    forward(100)
    left(60)

done()
