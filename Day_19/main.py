from turtle import *

tim = Turtle()
screen = Screen()

def moveforward():
    tim.fd(10)

def moveback():
    time.back(10)

def turnright():
    tim.right(10)

def turnleft():
    tim.left(10)

def reset():
    tim.clear()
    



screen.listen()
screen.onkey(key="w", fun=moveforward)
screen.onkey(key="s", fun=moveback)
screen.onkey(key="a", fun=turnleft)
screen.onkey(key="d", fun=turnright)
screen.onkey(key="c", fun=reset)

screen.exitonclick()