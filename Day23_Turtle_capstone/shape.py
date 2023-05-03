from turtle import Turtle

class Shape(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("black")
        self.penup()
        self.start()
        self.setheading(90)

    def start(self):
        self.goto(0, -280)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 10)
