import turtle
import pandas
from dateutil.parser import ParserError

FONT = ("Courier", 6, "normal")
image_path = "blank_states_img.gif"
csv_path = "50_states.csv"

screen = turtle.Screen()
screen.title("US States game")
screen.addshape(image_path)
turtle.shape(image_path)

data = pandas.read_csv(csv_path)
displayed_names=[]


def create_new_name (state_name, xcor, ycor) :
    name = turtle.Turtle()
    name.shapesize(0.1,0.1)
    name.penup()
    name.goto(xcor, ycor)
    
    name.write(state_name, True, align="center", font=FONT)
    return name

def get_mouse_click_coor(x, y):
    answer_state = screen.textinput(title=f'guess the state {len(displayed_names)}/50',prompt="enter the name ...").title()
    found_name = data[data.state==answer_state]
    if not found_name.empty:
        target_xcor = int(found_name.x)
        target_ycor = int(found_name.y)
        if x>target_xcor-10 and x<target_xcor+10:
            if y>target_ycor-10 and y<target_ycor+10:
                state_name = found_name['state'].values[0]
                displayed_names.append( create_new_name(state_name, target_xcor, target_ycor) )
                


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
