#draw a square

from turtle import Turtle, Screen

turtle = Turtle()

for i in range(50):
    turtle.forward(5)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()

screen = Screen()
screen.exitonclick()