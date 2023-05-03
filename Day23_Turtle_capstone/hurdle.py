import random
from turtle import Turtle
COLOR = ["black","green","yellow","red","blue","brown","grey"]

class Hurdle():
    def __init__(self):
        self.all_cars =[]
        self.speed=5
    def create_car(self):
        chance=random.randint(1,6)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLOR))
            new_car.penup()
            y_cor=random.randint(-240,240)
            new_car.goto(300,y_cor)
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars:
            cars.backward(self.speed)

    def speed_inc(self):
        self.speed += 5