from turtle import*
import time
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
start_pos =[(-10,0),(-30,0),(-50,0)]


segments = []

for body in start_pos:
    snake = Turtle("square")
    snake.penup()
    snake.color("white")
    snake.goto(body)
    segments.append(snake)











game_on = True

while game_on:
    screen.update()
    for parts in segments:
        parts.forward(20)
        
        time.sleep(0.1)

        for parts_num in range(len(segments)-1, 0, -1):
            new_x = segments[parts_num-1].xcor()
            new_y = segments[parts_num-1].ycor()
            segments[parts_num].goto(new_x,new_y)
        segments[0].forward(20)











screen.exitonclick()