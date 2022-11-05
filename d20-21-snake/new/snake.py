from turtle import Turtle

STARTING_POSITIONSL=[(0,0),(-20,0),(-40,0)]
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0),(-60,0),(-80,0),(-100,0),(-120,0),(-140,0),(-160,0)]

MOVING_DISTANCE=20

RIGHT=0
UP=90
LEFT=180
DOWN=270

class Snake():

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
        print("=====")
        print(self.segments)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def move(self):
        for seg_num in range( len(self.segments)-1, 0 , -1 ):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVING_DISTANCE)

    def add_segment(self, position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position() )

    def up(self):
        heading = self.head.heading()
        if heading!=DOWN:
            self.head.setheading(UP)
    
    def down(self):
        heading = self.head.heading()
        if heading!=UP:
            self.head.setheading(DOWN)

    def left(self):
        heading = self.head.heading()
        if heading!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        heading = self.head.heading()
        if heading!=LEFT:
            self.head.setheading(RIGHT)

    def collision_with_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment)<10:
                return True
        return False