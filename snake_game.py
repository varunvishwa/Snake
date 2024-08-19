from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")

game_on = True

screen.tracer(0)

snake1 = Snake()

food = Food()

score1 = Score()
score1.score = 0

screen.listen()

def move_up():
    if snake1.boxes[0].heading() != 270:
        snake1.boxes[0].setheading(90)

def move_down():
    if snake1.boxes[0].heading() != 90:
        snake1.boxes[0].setheading(270)

def move_left():
    if snake1.boxes[0].heading() != 0:
        snake1.boxes[0].setheading(180)

def move_right():
    if snake1.boxes[0].heading() != 180:
        snake1.boxes[0].setheading(0)

screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)


while game_on is True:
    screen.update()
    time.sleep(0.1)

    snake1.move_snake()

    if snake1.boxes[0].xcor() > 301 or snake1.boxes[0].ycor() > 301 or snake1.boxes[0].xcor() < -301 or snake1.boxes[0].ycor() < -301:
        game_on = False
    
    if (snake1.boxes[0].distance(food) < 15):
        print("NOM. NOM. NOM.")
        score1.increase_score()
        food.refresh()
        snake1.increase_length(snake1.boxes)

if game_on is False:
    pass



screen.exitonclick()
