from turtle import *



screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which tutle will win the race and enter the Color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]

print(user_bet)

for turtles in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtles])
    tim.goto(x=-230, y=y_pos[turtles])



screen.exitonclick()