from turtle import Turtle

from main import paddles

X_POS = 360
Y_POS = 0

class Paddle(Turtle):
    def __init__(self,size,pixel_size,speed):
        super().__init__()
        self.size = size
        self.pixel_size = pixel_size
        self.paddles = []
        self.paddle = None
        self.speed = speed

    #Create paddles
    def create_paddles(self):
        for n_paddles in range (-1, 2, 2) :
                self.paddle = Turtle()
                self.paddle.color("white")
                self.paddle.shape("square")
                self.paddle.speed(self.speed)
                self.paddle.shapesize(stretch_wid=5,stretch_len=1)
                self.paddle.penup()
                self.paddle.goto(X_POS*n_paddles,Y_POS)
                self.paddles.append(self.paddle)

        print("Paddles Created")
        print(self.paddles)
        return self.paddles

    def go_up(self,i):
        new_y = self.paddles[i].ycor()
        new_y += 20
        self.paddles[i]
