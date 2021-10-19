import turtle

turtle.bgcolor('black')

squary = turtle.Turtle()
squary.goto(0,0)
squary.pencolor("Yellow")
squary.speed(20)
squary.pensize(1)
for i in range(7):
    squary.right(90)
    squary.forward(1)
    for i in range(25):
        squary.forward(100)
        squary.left(55)

turtle.exitonclick()
