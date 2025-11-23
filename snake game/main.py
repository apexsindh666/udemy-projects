from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
gameon=True
while gameon:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        gameon=False
        scoreboard.game_over()

    for i in snake.segment[1:]:
        if snake.head.distance(i)<10:
            gameon=False
            scoreboard.game_over()




screen.exitonclick()