from turtle import *
from random import *
turtle = Turtle()
screen = Screen()
turtle.speed(0)

screen.colormode(255)

def move():
    turtle.fd(0.1)
    turtle.right(1)


while (True):
    
    turtle.color(randint(0,255), randint(0,255), randint(0,255))
    turtle.circle(200)
    move()
 



screen.exitonclick()


