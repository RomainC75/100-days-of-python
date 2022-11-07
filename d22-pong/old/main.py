from turtle import Turtle, Screen
from paddle import Paddle
import time

BOARD_DIMENSIONS=[ 800, 600 ]

screen = Screen()
screen.setup(width=BOARD_DIMENSIONS[0], height=BOARD_DIMENSIONS[1])
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

paddle=Paddle(BOARD_DIMENSIONS)

screen.listen() 
# screen.onkey(key="Up", fun=snake.up)
# screen.onkey(key="Down", fun=snake.down)
# screen.onkey(key="Left", fun=snake.left)
# screen.onkey(key="Right", fun=snake.right)

game_is_on=True


while game_is_on:
    screen.update()
    time.sleep(0.2)


screen.exitonclick()