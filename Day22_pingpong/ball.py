from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):

        self.color("white")
        self.shape("circle")
        self.penup()
        self.x=10
        self.y=10

    def move(self):
        xcor = self.xcor() + self.x
        ycor = self.ycor() + self.y
        self.goto(xcor, ycor)

    def bouncex(self):
        self.x *=-1

    def bouncey(self):
        self.y *= -1

    def reset(self):
        self.goto(0,0)
        self.bouncex()


