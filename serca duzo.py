
import turtle

turtle.bgcolor("pink")
ninja = turtle.Turtle()
ninja.color("red")

for i in range(10):

    ninja.left(90)
    ninja.circle(100,210)
    ninja.left(7)
    ninja.forward(260)

    ninja.left(95)
    ninja.forward(260)
    ninja.circle(100,220)
    ninja.left(96)
    ninja.penup()
    ninja.forward(400)
    ninja.pendown()

turtle.done()