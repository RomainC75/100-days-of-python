#draw a square

from turtle import Turtle, Screen
import random
from random import randrange


class Color:
    def __init__(self) -> None:
        self.colors = ["black","blue", "dark violet", "orange", "hot pink", "light blue", "black", "red", "green"]
        self.index = 0
    def get_color(self):
        current_color = self.colors[ self.index ]
        self.index = self.index+1 if self.index<len(self.colors)-1 else 0
        return current_color


color = Color()
turtle = Turtle()


directions = [0, 90, 180, 270, 360]


turtle.speed(0)
screen = Screen()
screen.colormode(255)

for n_gon in range(100):
    turtle.pencolor(color.get_color())
    turtle.circle( 100 )
    turtle.left(360/100)
    
screen.exitonclick()
