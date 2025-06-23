
import turtle


ninja = turtle.Turtle()
turtle.bgcolor("#8F8FBD")
ninja.speed(10)
ninja.color("black", "#ffcc00")

ninja.penup()
ninja.goto(0,-300)
ninja.pendown()

ninja.begin_fill()
ninja.circle(300,360)
ninja.end_fill()

ninja.penup()
ninja.goto(-150,-50)
ninja.right(90)
ninja.pendown()
ninja.circle(150,180)

ninja.penup()
ninja.goto(100,130)
ninja.pendown()
ninja.dot(10)

ninja.penup()
ninja.goto(-100,130)
ninja.pendown()
ninja.dot(10)

ninja.penup()
ninja.goto(-500,500)


turtle.done()