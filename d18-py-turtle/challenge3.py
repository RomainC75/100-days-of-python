#draw a square

from turtle import Turtle, Screen

turtle = Turtle()

colors=["black","blue", "dark violet", "orange", "hot pink", "light blue", "black", "red", "green"]
i=0

for n_gon in range(3,11):
    print(n_gon, i)
    turtle.pencolor(colors[i])
    i+=1
    for side in range(n_gon):
        turtle.right( (360/n_gon) )
        turtle.forward(100)

screen = Screen()
screen.exitonclick()