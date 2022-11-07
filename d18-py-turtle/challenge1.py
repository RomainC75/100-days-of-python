#draw a square

from turtle import Turtle, Screen

turtle = Turtle()

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

screen = Screen()
screen.exitonclick()