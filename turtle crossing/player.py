from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_f(self):
        if self.ycor() < FINISH_LINE_Y:
            return self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_b(self):
        if self.ycor() > -280:
            return self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
