from tkinter import *
from time import sleep

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
id=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    global id
    global reps
    reps=0
    print("id:",id)
    window.after_cancel(id)
    timer_title.config(text="Pomodoro")
    checkmark_label.config(text="")
    canvas.itemconfig(time_text,text='00:00')
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_time():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # work_sec = 2
    # short_break_sec = 2
    # long_break_sec = 2
    
    reps+=1

    work_indexes = [1,3,5,7]
    little_break_indexes = [2,4,6]
    if reps in work_indexes:
        count_down(work_sec)
        timer_title.config(text="Work !", fg=RED)
    elif reps in little_break_indexes:
        print("=>",int(reps/2), int(reps/2)*"✔")
        count_down(short_break_sec)
        timer_title.config(text="Rest :-)", fg=PINK)
        checkmark_label.config(text=int(reps/2)*"✔")
    elif reps==8:
        count_down(long_break_sec)
        timer_title.config(text="Big rest !!", fg=GREEN)
        checkmark_label.config(text="✔✔✔✔")
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global id
    print(count)
    minutes = count//60
    seconds = count%60
    print(minutes,seconds)
    minutes_str = str(minutes) if minutes>=10 else '0'+str(minutes)
    seconds_str = str(seconds) if seconds>=10 else '0'+str(seconds)

    canvas.itemconfig(time_text,text=f'{minutes_str}:{seconds_str}')
    if count>0:
        id = window.after(1000,count_down, count-1)
    else:
        start_time()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100,112, image=tomato_img)
time_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_title.grid(column=1, row=0)

checkmark_label = Label(text="", font=(FONT_NAME, 14, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_time)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command=reset_time)
reset_button.grid(column=2,row=2)


window.mainloop()
