from  turtle import *
from  random import *

turtle = Turtle()


for step in range(3,12):
    for steps in range(step):
        turtle.forward(100)
        turtle.right(180-(((step-2)*180)/step))





screen = Screen()
screen.exitonclick()


#120
#90
