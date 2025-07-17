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

#Create the  first paddle
paddles = Paddle(5,1,1)

screen.tracer(0)

game_on = True
paddles = paddles.create_paddles()


screen.listen()

while game_on:
    screen.update()
    #screen.onkey(paddles.go_up(),"Up")

    screen.exitonclick()
