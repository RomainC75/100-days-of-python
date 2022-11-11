from tkinter import *
from tkinter import messagebox
import pandas as pd
from pass_generator import get_random_pass

WHITE = "#ffffff"
LABEL_FONTS = ("Courier", 15, "normal")
MY_EMAIL = "rom.chenard@gmail.com"

try:
    file = open("pass.csv","r") 
    file.close()
except:
    file = open("pass.csv","w")
    first_line='website,email,pass\n'
    file.write(first_line)
    file.close()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = get_random_pass()
    password_input.delete(0,END)
    password_input.insert(END, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


    

def add_password():
    website_to_add = website_input.get()
    email_to_add = email_input.get()
    pass_to_add = password_input.get()

    if len(website_to_add)==0 or len(email_to_add)==0 or len(pass_to_add)==0:
        messagebox.showerror(title="validation problem",message="please, fill every fields")
        return

    isok=messagebox.askokcancel(title='do you confirm ? ', message=f'{website_to_add}-{email_to_add}-{pass_to_add}')

    if isok:
        new_dict= {
            "website":[website_to_add],
            "email":[email_to_add],
            "pass":[pass_to_add]
        }

        df1 = pd.read_csv("pass.csv")
        df2= pd.DataFrame(new_dict)
        df_final = pd.concat([df1,df2])
        df_final.to_csv('pass.csv',index_label=False)

        website_input.delete(0,END)
        password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_text = Label(text="Website:", font=LABEL_FONTS, bg=WHITE)
website_text.grid(column=0, row=1)
email_text = Label(text="Email/Username:", font=LABEL_FONTS, bg=WHITE)
email_text.grid(column=0, row=2)
password_text = Label(text="Password:", font=LABEL_FONTS, bg=WHITE)
password_text.grid(column=0, row=3)

#Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
#be ready to type !
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
#pre-insert the text - END is a tkinter constant
email_input.insert(END,string=MY_EMAIL)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# text.get("1.0", END)
# entry.insert(END, string="Some text to begin with.")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", command=add_password, width=36)
add_button.grid(column=1,row=4, columnspan=2)


window.mainloop()