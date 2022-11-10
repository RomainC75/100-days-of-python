from tkinter import *

window = Tk()
window.title("GUI program :-)")
window.minsize(width=500, height=300)
#add padding
window.config(padx=20, pady=20)

#Label
my_label = Label( text="Label", font=("Arial",24,"bold") )
#put on the screen 
my_label.config(text="new text")
# my_label.pack(side="left")
my_label.grid(column=0, row=0)

#change text
my_label['text']="New Text"

#Buttons
def button_clicked():
    print("clicked !")
    my_label.config(text=input.get())

button = Button(text="click on it!", command=button_clicked)
button.grid(column=1, row=1)

button2=Button(text="new button")
button2.grid(column=2, row=0)

#Entry
input = Entry(width=10)
text_inside = input.get()
input.grid(column=3,row=2)






window.mainloop()