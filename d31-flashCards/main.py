from tkinter import *
import pandas as pd
import random
import time

current_card={}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient= "records")
else:
    to_learn = data.to_dict(orient = "records")

global id

#==========functions===============
def next_card():
    global current_card
    global id
    canvas.after_cancel(id)

    current_card=random.choice(to_learn)
    current_card["French"]
    canvas.itemconfig(title,text="French")
    canvas.itemconfig(text,text=current_card["French"], fill="black")
    canvas.itemconfig(background, image=back_front)
    id =window.after(3000, func=flip_card )

def flip_card():
    global current_card
    global id
    
    canvas.itemconfig(title,text="English")
    canvas.itemconfig(text,text=current_card["English"], fill="white")
    canvas.itemconfig(background, image=back_back)

def next_and_remove_card():
    to_learn.remove(current_card)

    new_df = pd.DataFrame(to_learn)
    new_df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

#==========core=====================

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#canvas
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)

back_front = PhotoImage(file="./images/card_front.png")
back_back = PhotoImage(file="./images/card_back.png")
background = canvas.create_image(400,263, image=back_front)
title = canvas.create_text(400,150, text="French",font=("Ariel",40,'italic') )
text = canvas.create_text(400,263, text="Word",font=("Ariel",60,'bold') )

canvas.grid(row=0, column=0, columnspan=2)


wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0) 

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=next_and_remove_card)
right_button.grid(row=1, column=1) 
next_card()


window.mainloop()