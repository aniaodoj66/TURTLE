import turtle

ninja = turtle.Turtle()

pierwiastek = 2 ** 0.5

def kolko(x,y,t):
    t.penup()
    t.goto(x + 25 ,y)
    t.pendown()
    t.circle(25,360)

def krzyzyk(x,y,t):
    t.penup()
    t.goto(x + 25 ,y + 25)
    t.left(135)
    t.pendown()
    t.forward(50 * pierwiastek)

    t.penup()
    t.goto(x + 25 ,y - 25)
    t.right(90)
    t.pendown()
    t.forward(50 * pierwiastek)


krzyzyk(0,0,ninja)

turtle.done()