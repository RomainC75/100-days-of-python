from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

WINDOW_DIMENSIONS=[600,600]

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="turtle")
        self.penup()
        self.goto(*STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    
    def restart(self):
        self.goto(*STARTING_POSITION)