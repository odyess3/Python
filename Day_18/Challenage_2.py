from turtle import *
from random import *
turtle = Turtle()

def penup():
    turtle.penup()
def pendown():
    turtle.pendown()





for steps in range(1000):
    turtle.fd(steps)
    turtle.right(20)
    if steps%2==0:
        penup()
    else:
        pendown()
    


screen = Screen()
screen.exitonclick()


