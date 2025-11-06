from turtle import *

john = Turtle()

john.shape("turtle")
john.color("red")





for steps in range(4):
    john.forward(200)
    john.right(90)



screen =Screen()
screen.exitonclick()