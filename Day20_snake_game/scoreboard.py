import turtle
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def score_count(self):
        self.score += 1
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
