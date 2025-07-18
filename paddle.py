from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position,speed):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        self.speed = speed

    def go_up(self):
        y = self.ycor() + self.speed
        self.goto(self.xcor(),y)

    def go_down(self):
        y = self.ycor() - self.speed
        self.goto(self.xcor(),y)