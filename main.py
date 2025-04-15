from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collusion with food
    if snake.head.distance(food) < 16:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # detect collusion with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_on=False
        scoreboard.game_over()

   # detect collusion with its own tail.
    for each_segments in snake.snake_pieces[1:]:
        if snake.head.distance(each_segments) < 10:
           game_on=False
           scoreboard.game_over()


screen.exitonclick()