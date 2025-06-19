
import turtle
import time


ninja = turtle.Turtle()
turtle.bgcolor("pink")
ninja.color("brown")
ninja.speed(10)
ninja.dot(10)

# small circle
ninja.right(90)
ninja.penup()
ninja.forward(280)
ninja.pendown()
ninja.left(90)
ninja.circle(280,360)

# big circle
ninja.right(90)
ninja.penup()
ninja.forward(50)
ninja.pendown()
ninja.left(90)
ninja.circle(330,360)

# 6
ninja.write("6", align="center", font=("TimesNewRoman", 30, "normal"))

# 12
ninja.penup()
ninja.left(90)
ninja.forward(610)
ninja.pendown()
ninja.write("12", align="center", font=("TimesNewRoman", 30, "normal"))

# 3
ninja.penup()
ninja.goto(305,-10)
ninja.pendown()
ninja.write("3", align="center", font=("TimesNewRoman", 30, "normal"))

# 9
ninja.penup()
ninja.goto(-305,-10)
ninja.pendown()
ninja.write("9", align="center", font=("TimesNewRoman", 30, "normal"))

# time
current = time.strftime('%H:%M')
minute = int(current[-2:])
hour = int(current[:2])

# minute
ninja.penup()
ninja.goto(0,0)
ninja.pendown()
ninja.shape("arrow") 

angleMin = minute * 6
ninja.right(angleMin)
ninja.forward(230)

# hour
ninja2 = turtle.Turtle()
ninja2.color("brown")
ninja2.shape("arrow")
ninja2.penup()
ninja2.goto(0,0)
ninja2.pendown()
ninja2.setheading(90)
ninja2.shape("arrow")

angleHour = hour * 30 + 0.5 * minute
ninja2.right(angleHour)
ninja2.forward(130)


turtle.done()