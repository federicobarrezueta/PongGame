from turtle import Turtle
from field import Field

WIDTH = 10
HEIGHT = 100

X_POS = 360

class Paddle(Field):
    def __init__(self,size,pixel_size,speed):
        super().__init__()
        self.new_pixel = None
        self.field = Field().create_field()
        self.size = size
        self.pixel_size = pixel_size
        self.paddle_1 = []
        self.paddle_2 = []
        self.speed = speed
        self.field.update()
        self.create_paddles()


    #Create the first paddle
    def create_paddles(self):
        for n_paddles in range (-1, 1) :
            for i in range (0, self.size):
                self.new_pixel = Turtle()
                self.new_pixel.color("white")
                self.new_pixel.shape("square")
                self.new_pixel.speed(self.speed)
                self.new_pixel.shapesize(self.pixel_size)
                self.new_pixel.penup()
                self.new_pixel.goto(X_POS,(self.size*i + i*20)*n_paddles)
                if n_paddles == 0 :
                    self.paddle_1.append(self.new_pixel)
                elif n_paddles == 1:
                    self.paddle_2.append(self.new_pixel)

        print("Paddles Created")
