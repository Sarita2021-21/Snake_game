from turtle import Screen
import time
from snake_game import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
#detect a collision with food

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        # snake.segments+1
        
        

#  detect a collision with food
    if snake.head.xcor()<-290 or snake.head.xcor()>290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        is_game_on=False 
        print("Game over!")
        scoreboard.game_over()
           

    #collision  with tail
    
    for segments in snake.segments:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments)<10:
            is_game_on=False
            scoreboard.game_over()
screen.exitonclick()
