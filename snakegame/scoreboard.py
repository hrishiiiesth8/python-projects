from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        # self.high_score = self.read_score()
        self.color("red")
        self.penup()
        self.goto(0, 370)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def score_check(self):
        self.score += 1
        self.update()

    def reset_score(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()
        # self.data_new()

    # def data_new(self):
    #     with open("data.txt", mode="w") as file:
    #         file.write(str(self.high_score))
    #
    # @staticmethod
    # def read_score():
    #     with open("data.txt") as file2:
    #         contents = file2.read()
    #         return contents
