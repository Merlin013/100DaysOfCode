import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


jon = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(jon.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    jon.finish_line()
    car_manager.create_car()
    car_manager.move_cars()