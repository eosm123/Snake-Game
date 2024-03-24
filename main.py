from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #turn off the animation of the snake square moving to -40, 0 start pt

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()  # tell the program when to redraw and refresh the screen, move->update (repeat cycle)
    # update must come after tracer, if not nothing will update and be displayed on screen
    #put at this indentation to update when all the squares have moved -> snake moving as one piece
    time.sleep(0.1)  # 0.1s delay after all 3 segment moves
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        #game_is_on = False #removed due to continuing the game after losing
        #scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        # nid this if statement if not, it will detect the head as a segment to the head and just trigger game_over
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            #game_is_on = False
            #scoreboard.game_over()
    #if head collides with any segment in the tail:
        #trigger game_over

    #OR this below is better and less wordy
    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()







screen.exitonclick()