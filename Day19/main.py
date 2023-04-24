from turtle import Turtle,Screen
import random
def f():
    turtle.fd(10)
def a():
    turtle.bk(10)

def l():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)

def r():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)


turtle = Turtle()
screen = Screen()
screen.listen()
screen.onkey(f, "Up")
screen.onkey(a, "Down")
screen.onkey(l, "Left")
screen.onkey(r, "Right")

screen.exitonclick()