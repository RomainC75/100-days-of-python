from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = [ "red", "orange", "yellow", "green", "blue", "purple" ]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? enter your color: ")
print(user_bet)

turtles = []
for i in range(6):
    newT = Turtle(shape="turtle")
    newT.penup()
    newT.color(colors[i])
    newT.goto(x=-240,y=125-i*50)
    newT.shapesize(stretch_wid=1.5)
    turtles.append(newT)
    print(newT.position())

j=0
while True:
    turtles[j%6].forward( random.randint(1,30) )
    print(turtles[j%6].position())
    if turtles[j%6].position()[0]>=240:
        print(f'winner : {colors[j%6]}')
        if(user_bet == turtles[j%6].color()[0]):
            print("you won !!")
        else :
            print("looser !")
        # print(f'your bet : {user_bet}, {turtles[j%6].color()[0]}')
        break
    j+=1

screen.exitonclick()