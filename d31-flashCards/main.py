from tkinter import *
import pandas as pd
import random

try:
    data = pd.read_csv("./data/french_words.csv")
except FileNotFoundError:
    print("./data/french_words.csv doesn't exist")

data_to_use=[]

for (index,row) in data.iterrows() : 
    data_to_use.append([ row[0], row[1] ] )
print(data_to_use)

#==========functions===============
def get_random_values():
    values = random.choice(data_to_use)
    canvas.itemconfig(question,text=values[1])
    canvas.itemconfig(answer,text=values[0])


#==========core=====================


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#canvas
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)

back_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400,263, image=back_front)
back_back = PhotoImage(file="./images/card_back.png")
canvas.create_image(400,263, image=back_back)
question = canvas.create_text(400,150, text="French",font=("Ariel",40,'italic') )
answer = canvas.create_text(400,263, text="Word",font=("Ariel",60,'bold') )

canvas.grid(row=0, column=0, columnspan=2)


wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0)
wrong_button.grid(row=1, column=0) 

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=get_random_values)
right_button.grid(row=1, column=1) 



window.mainloop()