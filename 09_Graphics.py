import turtle as t
t.bgcolor('black')
color = ('pink','green','blue','cyan','deepskyblue','white','red')
for i in range(250):
    t.pencolor(color[i%7])
    t.speed(0)

    t.left(30)
    t.forward(i)
    t.speed(0)
    t.right(120)
    t.forward(i)
    t.right(320)

    t.right(190)
    t.forward(i)

t.done()
