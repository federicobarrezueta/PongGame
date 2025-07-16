#Classes for this game
#field
#pongs
#ball
#scoreboard

#1 - Create Screen
#2 - Create and move paddle
#3 - Create and move ball
#4 -

from field import Field
from paddle import Paddle
import time

#Create the field
#field = Field()

#Create the  first paddle
paddles = Paddle(5,1,1)

paddles.field.exitonclick()
