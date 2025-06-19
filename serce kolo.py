
import turtle

turtle.bgcolor("pink")
ninja = turtle.Turtle()
ninja.color("red")
ninja.speed(100)
ninja.left(90)
ninja.penup()
ninja.forward(100)
ninja.pendown()
ninja.right(90)

for i in range(180):
    ninja.left(90)
    ninja.circle(100,210)
    ninja.left(7)
    ninja.forward(260)

    ninja.left(95)
    ninja.forward(260)
    ninja.circle(100,220)

    ninja.left(100)

turtle.done()