from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
dimensions = [600,600]

screen = Screen()
screen.setup(width=dimensions[0], height=dimensions[1])
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()

food=Food(dimensions[0], dimensions[1], snake_arr=snake.snake)
# food.color("red")

points=0


screen.listen() 
screen.onkey(key="q", fun=snake.turn_left)
screen.onkey(key="d", fun=snake.turn_right)
# screen.onkey(key="c", fun=reset)

def is_head_on_food(snake,food):
    head_position=snake.get_head_position()
    food_position = food.get_food_position()
    if round(head_position[0])==round(food_position[0]) and round(head_position[1])==round(food_position[1]):
        return True
    return False



print(f'arr: {snake.snake}')
print(f'food position : {food.coord}')
while True:
    screen.update()
    time.sleep(0.2)
    if not snake.move():
        print("FINISHED !!")
        screen.bye()
    head_coord=snake.get_head_position()
    print(f'head position : {head_coord}')
    # if head_coord[0]>dimensions[0]/2 or head_coord[0]<-dimensions[0]/2 or head_coord[1]>dimensions[1]/2 or head_coord[1]<-dimensions[1]/2 :
    #     screen.bye()
    if is_head_on_food(snake,food):
        snake.just_eat()
        food.get_new_position(snake_arr=snake.snake)
        points+=1
        print("++points",points,"+++")
        print("call just_eat")
        
    
        
        

screen.exitonclick()