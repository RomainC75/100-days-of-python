from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self) -> None:
        self.level=1
        self.level_display=Turtle()
        self.level_display.penup()
        self.level_display.shapesize(0.1,0.1)
        self.level_display.penup()
        self.level_display.goto(-110,260)
        self.display_level()

        self.game_over=Turtle()
        self.game_over.penup()
        self.game_over.goto(-30,30)
        self.game_over.color("white")

    def display_level(self):
        self.level_display.clear()
        self.level_display.write(f'level : {self.level}', True, align="right", font=FONT)

    def display_gameover(self):
        self.game_over.color("black")
        self.game_over.write(f'GAME OVER', True, align="right", font=FONT)
    
    def levelup(self):
        self.level+=1
        self.display_level()


        