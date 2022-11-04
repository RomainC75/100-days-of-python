from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(50)

screen.listen() 
screen.onkey(key="Up", fun=move_forward)
screen.exitonclick()