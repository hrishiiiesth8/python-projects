from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new = self.ycor() + 40
        return self.goto(self.xcor(), new)

    def go_down(self):
        new = self.ycor() - 40
        return self.goto(self.xcor(), new)
