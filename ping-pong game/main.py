import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.title("PONG")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
pong = Ball()
scores = Score()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    pong.move()
    time.sleep(pong.move_speed)
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()

    if pong.distance(l_paddle) < 50 and pong.xcor() < -320 or \
            pong.distance(r_paddle) < 50 and pong.xcor() > 320:
        pong.bounce_x()

    if pong.xcor() > 380:
        scores.l_point()
        pong.reset_position()

    if pong.xcor() < -380:
        scores.r_point()
        pong.reset_position()

    screen.update()

screen.exitonclick()
