
from turtle import Turtle
STARTING_POSITIONS=[(350, 0),(-350,0)]
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles=[]
        self.paddle = Turtle()
        self.create_paddle()
        self.paddle1 =self.paddles[0]
        self.paddle2 = self.paddles[1]

    def create_paddle(self):
        for segments in STARTING_POSITIONS:
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.shapesize(5, 1)
            segment.penup()
            segment.goto(segments)
            self.paddles.append(segment)

    def up(self):
        self.paddle1.goto(self.paddle1.xcor(), self.paddle1.ycor() + 20)

    def down(self):
        self.paddle1.goto(self.paddle1.xcor(), self.paddle1.ycor() - 20)

    def up1(self):
        self.paddle2.goto(self.paddle2.xcor(), self.paddle2.ycor() + 20)

    def down1(self):
        self.paddle2.goto(self.paddle2.xcor(), self.paddle2.ycor() - 20)


