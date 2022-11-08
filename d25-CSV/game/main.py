import turtle
import pandas

FONT = ("Courier", 6, "normal")
image_path = "blank_states_img.gif"
csv_path = "50_states.csv"

screen = turtle.Screen()
screen.title("US States game")
screen.addshape(image_path)
turtle.shape(image_path)

data = pandas.read_csv(csv_path)
displayed_names=[]

def record_false_answers():
    missing=[]
    for state in data['state'].to_list():
        if state not in displayed_names:
            missing.append(state)
    new_data = pandas.DataFrame(missing)
    new_data.to_csv("work_again.csv")

def create_new_name (state_name, xcor, ycor) :
    name = turtle.Turtle()
    name.shapesize(0.1,0.1)
    name.penup()
    name.goto(xcor, ycor)    
    name.write(state_name, True, align="center", font=FONT)
    return name

def get_mouse_click_coor(x, y):
    answer_state = screen.textinput(title=f'guess the state {len(displayed_names)}/50',prompt="enter the name ...").title()
    if answer_state=="Exit":
        record_false_answers()
        exit()
    found_name = data[data.state==answer_state]
    if not found_name.empty:
        target_xcor = int(found_name.x)
        target_ycor = int(found_name.y)
        if x>target_xcor-20 and x<target_xcor+20:
            if y>target_ycor-20 and y<target_ycor+20:
                state_name = found_name['state'].values[0]
                create_new_name(state_name, target_xcor, target_ycor) 
                displayed_names.append( state_name )
    
    if len(displayed_names)==50:
        print("congrats ! You won ! ")
        exit()


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
