import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player= Player()

scoreboard=Scoreboard()
screen.listen()
screen.onkey(key="Up",fun=player.move)

car_manager = CarManager()

def restart():
    time.sleep(1)
    scoreboard.levelup()
    player.restart()
    car_manager.restart_cars()

game_is_on = True

while game_is_on:
    time.sleep(0.1)    
    car_manager.move()
    screen.update()
    if car_manager.isCollision(player.ycor()):
        game_is_on=False
        scoreboard.display_gameover()

    if player.ycor()>280:
        restart()

screen.exitonclick()