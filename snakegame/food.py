from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.refresh()

    def refresh(self):
        ran_x = randint(-380, 380)
        ran_y = randint(-380, 380)
        self.goto(ran_x, ran_y)
