import turtle
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=0

    def score_count(self):
        self.score += 1
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score} High Score : {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        self.clear()
        if self.score >= self.high_score:
            self.high_score=self.score
        self.score=0
        self.update_score()




    #def game_over(self):
        #self.goto(0, 0)
        #self.color("white")
        #self.penup()
        #self.hideturtle()
        #self.write("Game Over", align="center", font=("Arial", 24, "normal"))
