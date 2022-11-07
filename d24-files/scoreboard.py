from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.init_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} / high score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score=0
        self.update_scoreboard()
        self.init_high_score()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def init_high_score(self):
        try:
            with open("data.txt") as file:
                self.high_score=int(file.read())
        except:
            self.high_score= 3
            print("no data file !")
        
