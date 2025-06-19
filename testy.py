import turtle
import time

ninja = turtle.Turtle()

# time
current = time.strftime('%H:%M')
minute = int(current[-2:])
hour = int(current[:2])
# minute
ninja.penup()
ninja.goto(0,0)
ninja.pendown()

angleMin = minute * 6
ninja.right(angleMin)
ninja.forward(200)

turtle.done()