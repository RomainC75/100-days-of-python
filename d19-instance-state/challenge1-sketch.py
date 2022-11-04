from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def reset():
    # tim.reset()
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

screen.listen() 
screen.onkey(key="z", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="q", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)


screen.exitonclick()