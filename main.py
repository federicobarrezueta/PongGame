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
from ball import Ball
from scoreboard import Scoreboard
import time

#Create screen and configs
screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong!")
print("Field Created")
screen.tracer(0)

#Create the paddles
r_paddle = Paddle((350,0),30)
l_paddle = Paddle((-350,0),30)

#Create the ball
ball = Ball()

#Create the scoreboard
scoreboard = Scoreboard()

#Listen to keystrokes
screen.listen()

#Paddle movement control
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

#Keep playing until game is on
game_on = True



while game_on:

    time.sleep(0.01)
    #Moves the ball
    ball.move()

    #Bounces when hit
    has_bounced = ball.bounce(r_paddle,l_paddle)

    #Detects misses and increases the score accordingly
    if has_bounced == -1:
        scoreboard.l_point()
    if has_bounced == 1:
        scoreboard.r_point()

    #Resets the game if the ball leaves the field
    ball.reset_game()

    screen.update()


screen.exitonclick()
