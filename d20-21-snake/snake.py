from turtle import Turtle

class Snake:
    def __init__(self, length=15) -> None:
        self.snake=[]
        self.length=length
        self.start_position()
        self.just_ate=False

    def start_position(self):
        for i in range(self.length):
            turtle=Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=-i*20,y=0)
            # turtle.tracer
            self.snake.append(turtle)
            
    def turn_right(self):
        self.snake[0].right(90)

    def turn_left(self):
        self.snake[0].left(90)

    def just_eat(self):
        self.just_ate=True

    def create_new_square(self, last_coord):
        new = Turtle(shape="square")
        new.color("white")
        new.penup()
        new.goto(*last_coord)
        self.snake.append(new)
        print("==>",len(self.snake))

    def move(self):
        
        for i in range(len(self.snake))[::-1]:
            if i==0 :
                self.snake[i].forward(20)
            elif (self.just_ate and i==len(self.snake)-1):
                self.snake.append(self.snake[len(self.snake)-1])
                last_coord = [self.snake[i].position()[0], self.snake[i].position()[1]]
                self.snake[i].goto( self.snake[i-1].position()[0], self.snake[i-1].position()[1] )
                self.create_new_square(last_coord)
                print("==============FOOD  ============")
                self.just_ate=False    
            else:
                self.snake[i].goto( self.snake[i-1].position()[0], self.snake[i-1].position()[1] )
            #blocked by walls
        if self.snake[0].position()[0]>300 or self.snake[0].position()[0]<-300 or self.snake[0].position()[1]>300 or self.snake[0].position()[1]<-300:
            print("outside !")
            return False
        if self.is_blocked_by_body():
            print("blocked by body!!")
            return False
        return True

    def get_head_position(self):
        return self.snake[0].position()

    def is_blocked_by_body(self):
        positions = [ coords for coords in map( lambda x:( round(x.position()[0]), round(x.position()[1]) ), self.snake ) ]
        head_position=positions[0]
        positions = positions[1:]
        if head_position in positions:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
            return True
        print("positions",positions)
        return False