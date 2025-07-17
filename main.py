#Classes for this game
#field
#pongs
#ball
#scoreboard

#1 - Create Screen
#2 - Create and move paddle
#3 - Create and move ball
#4 -
WIDTH = 800
HEIGHT = 600

from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong!")
print("Field Created")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
