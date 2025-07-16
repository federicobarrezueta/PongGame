from turtle import Turtle, Screen

WIDTH = 800
HEIGHT = 600





class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.field = Screen()

    def create_field(self):
        self.field.bgcolor("black")
        self.field.setup(width=WIDTH,height=HEIGHT)
        self.field.title("Pong!")
        print("Field Created")

        #The screen is ended on the main
        #self.field.exitonclick()
        return self.field