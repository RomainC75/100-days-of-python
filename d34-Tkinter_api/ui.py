from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT=("Arial",20,"italic")


class QuizInterface():
    
        

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window=Tk()
        self.window.title("quizz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text=self.canvas.create_text(150,125, text="super question !", fill="black", font=FONT, width=280)
        self.canvas.grid(row=1,column=0, columnspan=2, pady=20)

        self.score = Label(text="Score:0", fg="#ffffff", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        #+command
        self.true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_button_image, highlightthickness=0, command=self.set_True)
        self.true_button.grid(row=2, column=0)

        self.false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_button_image, highlightthickness=0, command=self.set_False)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        id=self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            txt = self.quiz.next_question()
            print("==>txt ", txt)
            self.canvas.itemconfig(self.question_text,text=txt)
        else:
            self.canvas.itemconfig(self.question_text,text="finished !")
            #disable buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def set_True(self):
        is_right=self.quiz.check_answer("true")
        self.score.config(text=f"score:{self.quiz.score}/{self.quiz.question_number}")
        self.change_bg_color(is_right)
    
    def set_False(self):
        is_right=self.quiz.check_answer("false")
        self.score.config(text=f"score:{self.quiz.score}/{self.quiz.question_number}")
        self.change_bg_color(is_right)

    def change_bg_color(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.configure(bg="red")
        id=self.window.after(1000,func=self.get_next_question)
        
