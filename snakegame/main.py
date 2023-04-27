import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

# s1 = Turtle("square")
# s1.color("white")
# s2 = Turtle("square")
# s2.color("white")
# s2.goto(x=-20, y=0)
# s3 = Turtle("square")
# s3.color("white")
# s3.goto(x=-40, y=0)

mys = Screen()
mys.setup(width=800, height=800)
mys.bgcolor("black")
mys.title("Snake Game")
mys.tracer(0)

cobra = Snake()
food = Food()
score = Scoreboard()

mys.listen()
mys.onkey(cobra.up, "Up")
mys.onkey(cobra.down, "Down")
mys.onkey(cobra.right, "Right")
mys.onkey(cobra.left, "Left")

game_on = True
while game_on:
    mys.update()
    time.sleep(0.1)
    cobra.move()

    if cobra.head.distance(food) < 15:
        food.refresh()
        cobra.extend()
        score.score_check()

    if cobra.head.xcor() > 380 or cobra.head.xcor() < -380 \
            or cobra.head.ycor() > 380 or cobra.head.ycor() < -380:
        score.reset_score()
        cobra.reset_snake()

    for seg in cobra.segments:
        if seg == cobra.head:
            pass
        elif cobra.head.distance(seg) < 10:
            score.reset_score()
            cobra.reset_snake()

mys.exitonclick()
