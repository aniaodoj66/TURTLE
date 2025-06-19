import turtle

turtle.bgcolor('black')

t = turtle.Turtle()

colors = ['red', 'dark red']

turtle.speed(900)

for numbers in range(400):

  t.forward(numbers + 1)

  t.right(89)

  t.pencolor(colors[numbers % 2])

turtle.done()