from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, width, height, snake_arr) -> None:
        super().__init__(shape="square")
        self.width=width
        self.height=height
        self.coord = self.get_new_position(snake_arr)
        self.color("red")
        self.penup()

    def get_new_position(self, snake_arr):
        witness=True
        while witness:
            witness=False
            x=random.randint( int(self.width/-2), int(self.width/2)+1 )
            y=random.randint( int(self.height/-2) , int(self.height/2)+1 )
            coord=[ x-x%20, y-y%20  ]
            for square in snake_arr:
                if square.position()[0]==coord[0] and square.position()[1]==coord[1]:
                    witness=True
            print(coord, witness)
        self.coord=coord
        print(coord,"//",*coord)
        super().goto(*coord)
        return coord

    def get_food_position(self):
        return self.coord
    