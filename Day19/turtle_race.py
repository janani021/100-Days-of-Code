import random
from turtle import Turtle, Screen

screen = Screen()
selected_colour = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtle = Turtle()
turtle1 = Turtle()
turtle2 = Turtle()

turtle.shape("turtle")
turtle.color("red")
turtle.penup()
turtle.setposition(-180, 180)

turtle1.shape("turtle")
turtle1.color("green")
turtle1.penup()
turtle1.setposition(-180, 0)

turtle2.shape("turtle")
turtle2.color("blue")
turtle2.penup()
turtle2.setposition(-180, -180)

flag = True
while (flag == True):
    turtle.forward(random.randint(1, 10))
    turtle1.forward(random.randint(1, 10))
    turtle2.forward(random.randint(1, 10))

    if (turtle.position()[0] >= 200 or turtle1.position()[0] >= 200 or turtle2.position()[0] >= 200):
        if (turtle.position()[0] > turtle1.position()[0] and turtle.position()[0] > turtle2.position()[0]):
            colour = "red"
            print("Red is the winner")
        elif (turtle1.position()[0] > turtle.position()[0] and turtle1.position()[0] > turtle2.position()[0]):
            colour = "green"
            print("Green is the winner")
        else:
            colour = "blue"
            print("Green is the winner")

        flag = False
        if selected_colour == colour:
            print("You guessed correctly")
        else:
            print("You lose! You guessed wrongly")
screen.exitonclick()
