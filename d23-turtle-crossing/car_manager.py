from turtle import Turtle
import random
WINDOW_DIMENSIONS=[600,600]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

def mapCars(car):
    if car.xcor() < -WINDOW_DIMENSIONS[0]/2-20:
        return 0
    else:
        return car

class CarManager:
    def __init__(self, level=1) -> None:
        self.cars=[]
        self.starting_Xposition=WINDOW_DIMENSIONS[0]/2
        self.level=level
        self.speed=STARTING_MOVE_DISTANCE*level
        
    def create_new_car(self):
        new_car=Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=1.8)
        new_car.penup()
        new_car.setheading(180)
        new_car.color( random.choice(COLORS) )
        new_car.goto( self.starting_Xposition, random.randint(-WINDOW_DIMENSIONS[1]/2+30, WINDOW_DIMENSIONS[1]/2))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            print("car")
            car.forward( self.speed )
        self.cars= list(map( lambda car : mapCars(car),self.cars))
        self.cars=list( filter( lambda car: car!=0, self.cars ) ) 
        if( random.randint(0,10) <= 2 ):
            self.create_new_car()
        print( "Length : ", len(self.cars) )


    def isCollision(self, turtle_Yposition):
        for car in self.cars:
            print(car)
            if car.xcor()<15 and car.xcor()>-15:
                print("car : ", car.position())
            if car.xcor()<15 and car.xcor()>-15 and car.ycor()>turtle_Yposition-10 and car.ycor()<turtle_Yposition+10:
                print( "position : ", car.position() )
                return True
        return False

    def restart_cars(self):
        for car in self.cars:
            car.goto(-600,0)
        self.cars=[]
        self.speed+=MOVE_INCREMENT

