from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize()
        self.penup()
        self.speed = 1
        self.x_move = self.speed
        self.y_move = self.speed

    def move(self):
        new_x = self.xcor() + self.x_move * self.speed
        new_y = self.ycor() + self.y_move * self.speed
        self.goto(new_x,new_y)

    def bounce(self,r_paddle,l_paddle):
        #Detect collision with top and bottom wall
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1
            print(self.speed)

        #Detect collision with a paddle
        if ((self.distance(r_paddle) < 50 and self.xcor() > 320)
                or (self.distance(l_paddle) < 50 and self.xcor() < -320)):
            self.x_move *= -1
            self.speed += 0.25
            print(self.speed)

        #Detects is a paddle misses and returns a value to increase the score
        if self.xcor() > 400 :
            print("Hit Right wall")
            return 1

        elif self.xcor() < -400 :
            print("Hit Left wall")
            return -1

        else :
            return None

    def reset_game(self):
        if self.xcor() > 400 or self.xcor() < -400:
            time.sleep(1)
            #Initializes the ball position
            self.setposition(0,0)
            #Changes the ball direction
            self.x_move *= -1
            #Resets the ball speed
            self.speed = 3