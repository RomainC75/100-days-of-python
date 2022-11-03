###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
from turtle import Turtle, Screen

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)
print("colors in the jpeg : ",rgb_colors)

turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.penup()
turtle.hideturtle()
turtle.speed(0)

dimensions = [30, 15, 40]

#initial position
turtle.backward(dimensions[0]*dimensions[2]/2)
turtle.left(90)
turtle.forward(dimensions[1]*dimensions[2]/2)
turtle.right(90)

for i in range(dimensions[1]):

    for j in range(dimensions[0]):
        selected_color = random.choice(rgb_colors)
        turtle.dot(20, (selected_color.r,selected_color.g,selected_color.b) )
        turtle.forward(dimensions[2])
    
    turtle.backward(dimensions[0]*dimensions[2])
    turtle.right(90)
    turtle.forward(dimensions[2])
    turtle.left(90)


screen.exitonclick()