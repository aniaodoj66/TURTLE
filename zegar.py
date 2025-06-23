
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

# 12
ninja.penup()
ninja.goto(0,283)
ninja.pendown()
ninja.write("12", align="center", font=("Times New Roman", 30, "normal"))

# 1
ninja.penup()
ninja.goto(145,245)
ninja.pendown()
ninja.write("1", align="center", font=("Times New Roman", 30, "normal"))

# 2 
ninja.penup()
ninja.goto(255,150)
ninja.pendown()
ninja.write("2", align="center", font=("Times New Roman", 30, "normal"))

# 3
ninja.penup()
ninja.goto(305,-10)
ninja.pendown()
ninja.write("3", align="center", font=("Times New Roman", 30, "normal"))

# 4 
ninja.penup()
ninja.goto(255,-185)
ninja.pendown()
ninja.write("4", align="center", font=("Times New Roman", 30, "normal"))

# 5
ninja.penup()
ninja.goto(140,-295)
ninja.pendown()
ninja.write("5", align="center", font=("Times New Roman", 30, "normal"))

# 6
ninja.penup()
ninja.goto(0,-330)
ninja.pendown()
ninja.write("6", align="center", font=("Times New Roman", 30, "normal"))

# 7
ninja.penup()
ninja.goto(-140,-295)
ninja.pendown()
ninja.write("7", align="center", font=("Times New Roman", 30, "normal"))

# 8 
ninja.penup()
ninja.goto(-255,-185)
ninja.pendown()
ninja.write("8", align="center", font=("Times New Roman", 30, "normal"))

# 9
ninja.penup()
ninja.goto(-305,-10)
ninja.pendown()
ninja.write("9", align="center", font=("Times New Roman", 30, "normal"))

# 10 
ninja.penup()
ninja.goto(-250,150)
ninja.pendown()
ninja.write("10", align="center", font=("Times New Roman", 30, "normal"))

# 11
ninja.penup()
ninja.goto(-140,245)
ninja.pendown()
ninja.write("11", align="center", font=("Times New Roman", 30, "normal"))

# time
current = time.strftime('%H:%M')
minute = int(current[-2:])
hour = int(current[:2])

# minute
ninja.penup()
ninja.goto(0,0)
ninja.pendown()
ninja.shape("arrow") 

angleMin = minute * 6 - 90
ninja.right(angleMin)
ninja.forward(230)

# hour
ninja2 = turtle.Turtle()
ninja2.color("brown")
ninja2.shape("arrow")
ninja2.penup()
ninja2.goto(0,0)
ninja2.pendown()

ninja2.shape("arrow")

angleHour = hour * 30 + 0.5 * minute - 90
ninja2.right(angleHour)
ninja2.forward(130)


turtle.done()