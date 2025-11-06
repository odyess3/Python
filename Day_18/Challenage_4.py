from turtle import *
from random import *
turtle = Turtle()
screen = Screen()

screen.colormode(255)

def up():
    turtle.setheading(90)
    turtle.fd(50)

def right():
    turtle.setheading(0)
    turtle.fd(50)

def left():
    turtle.setheading(180)
    turtle.fd(50)

def down():
    turtle.setheading(270)
    turtle.fd(50)



up()
down()
right()
down()
left()

while (True):
    random = randint(0,3)
    turtle.color(randint(0,255), randint(0,255), randint(0,255))
    if random == 0:
        up()
    elif random == 1:
        right()
    elif random == 2:
        left()
    elif random == 3:
        down()



screen.exitonclick()


