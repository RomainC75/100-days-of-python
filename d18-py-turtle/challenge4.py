#draw a square

from turtle import Turtle, Screen
import random
from random import randrange

turtle = Turtle()

colors=["black","blue", "dark violet", "orange", "hot pink", "light blue", "black", "red", "green"]
directions = [0, 90, 180, 270, 360]
i=0

def random_color():
    r = randrange(1,255)
    g = randrange(1,255)
    b = randrange(1,255)
    return (r,g,b)

turtle.pensize(15)
turtle.speed(0)
screen = Screen()
screen.colormode(255)

for n_gon in range(1000):
    # turtle.pencolor( colors[random.randrange(0,len(colors))] )
    turtle.pencolor( random_color() )
    turtle.right( random.choice(directions) )
    turtle.forward(20)
    


screen.exitonclick()