
import turtle

turtle.bgcolor("yellow")
ninja = turtle.Turtle()
ninja.color("blue")
ninja.speed(100)

for i in range(100):
    ninja.left(90)
    ninja.circle(100,210)
    ninja.left(7)
    ninja.forward(260)

    ninja.left(95)
    ninja.forward(260)
    ninja.circle(100,220)

    ninja.left(10)
    
    if i % 2 == 0:
        ninja.color("green")
    else:
        ninja.color("blue")

turtle.done()