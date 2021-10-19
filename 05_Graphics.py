import time
import turtle
import random
screen = turtle.Screen()
bob = turtle.Turtle()
screen.bgcolor("black")
bob.pencolor("Aquamarine")
bob.speed(100)
def crazy(var1):
    for i in range(250):
        bob.forward(i)
        bob.left(var1)


crazy(300)
time.sleep(5)
