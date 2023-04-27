import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_factory = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_f, "Up")
screen.onkey(player.move_b, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_factory.create_car()
    car_factory.move_cars()

    for any_car in car_factory.all_cars:
        if any_car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 230:
        player.goto(0, -280)
        car_factory.level_up()
        scoreboard.increase_level()


screen.exitonclick()
