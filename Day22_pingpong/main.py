from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
score = Scoreboard()

screen.listen()
paddle.speed("fastest")
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle.up1, "w")
screen.onkey(paddle.down1, "s")

paddle1 = paddle.paddle1
paddle2 = paddle.paddle2
flag = True
while flag:
    screen.update()
    time.sleep(0.1)
    ball.move()
    paddle.speed("fastest")

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bouncex()


    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick()
