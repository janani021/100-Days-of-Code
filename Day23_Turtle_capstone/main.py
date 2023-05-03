from turtle import Screen
from shape import Shape
from hurdle import Hurdle
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Race")
screen.tracer(0)

turtle = Shape()
hurdle = Hurdle()
score = Score()

screen.listen()
screen.onkey(turtle.up, "Up")


flag = True
while flag:
    screen.update()
    time.sleep(0.1)
    hurdle.create_car()
    hurdle.move()

    if turtle.ycor() >= 280:
        turtle.start()
        hurdle.speed_inc()
        score.increase_level()

    for cars in hurdle.all_cars:
        if cars.distance(turtle) < 22:
            score.game_over()
            flag=False

screen.exitonclick()
