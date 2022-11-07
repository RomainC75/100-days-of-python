from turtle import Turtle

START_POSITION = [ (260,40),(260,20),(260,0), (260,-20),(260,-40) ]

class Paddle():
    def __init__( self, board_dimensions, player ) -> None:
        self.barre=[]
        self.init_barre()
        self.board_dimensions = board_dimensions
        self.start_positions = []

    def init_barre(self):
        for sq in START_POSITION:
            square=Turtle()
            square.shape( "square" )
            square.color( "white" )
            square.penup()
            square.goto( *sq )
            self.barre.append(square)
