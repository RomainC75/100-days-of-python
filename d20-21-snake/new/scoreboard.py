from turtle import Turtle
ALIGNEMENT= "center"
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="circle", visible=False)
        self.penup()        
        self.color("white")
        self.shapesize(0.1, 0.1)
        self.points=0
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.goto(-40,260)
        self.write(f'Score = {self.points}', True, align=ALIGNEMENT, font=FONT)

    def scoreUp(self):
        self.points+=1
        self.updateScore()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f'GAME OVER ! {self.points} points', True, align=ALIGNEMENT, font=FONT)