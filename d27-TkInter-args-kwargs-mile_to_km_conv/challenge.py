from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles -> Km converter")
window.minsize(width=300, height=150)
window.config(padx=30, pady=30)

is_equal_label = Label( text="is equal to", font=("Arial",15,"bold") )
is_equal_label.grid(column=0, row=1)

input = Entry(width=7)
input.grid(column=1,row=0)

result =Label( text="0", font=("Arial",15,"bold") )
result.grid(column=1,row=1)

def print_result():
    try:
        miles = int(input.get())*1.6
        result.config(text="%.2f"%miles)
    except:
        print("not a number ^^")


calculate_button = Button(text="Calculate", command=print_result)
calculate_button.grid(column=1, row=2)

miles_label = Label( text="Miles", font=("Arial",15,"bold") )
miles_label.grid(column=2, row=0)

km_label = Label( text="km", font=("Arial",15,"bold") )
km_label.grid(column=2, row=1)




window.mainloop()