import random
from turtle import Turtle, Screen
from border import Border
from ball import Ball
from paddles import Paddle
import time
from scoreboard import Scoreboard
from ball import MOVE_DISTANCE

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(700, 700)
screen.tracer(0)

border_t = Border()
border_t.goto(0, 300)
border_b = Border()
border_b.goto(0, -300)

ball = Ball()
rand_numb = random.randint(-45, 45)
ball.seth(rand_numb)

paddle_l = Paddle()
paddle_r = Paddle()
paddle_l.goto(-300, -130)
paddle_r.goto(300, 130)

mid = Turtle()
mid.shape("square")
mid.color("white")
mid.hideturtle()
mid.pu()
mid.goto(0, -290)
mid.pensize(10)
mid.seth(90)
for i in range(20):
    mid.pd()
    mid.forward(10)
    mid.pu()
    mid.forward(20)

scoreboard_r = Scoreboard()
scoreboard_l = Scoreboard()
scoreboard = Scoreboard()
scoreboard_r.goto(70, 300)
scoreboard_l.goto(-70, 300)
scoreboard_l.print_scoreboard()
scoreboard_r.print_scoreboard()

screen.listen()
screen.onkeypress(paddle_r.move_up, "Down")
screen.onkeypress(paddle_r.move_down, "Up")
screen.onkeypress(paddle_l.move_up, "s")
screen.onkeypress(paddle_l.move_down, "w")

game_going = True
while game_going:
    time_sleep = 0.04
    time.sleep(time_sleep)
    screen.update()

    ball.move()
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    paddle_r_x = paddle_r.xcor()
    paddle_r_y = paddle_r.ycor()
    paddle_l_x = paddle_l.xcor()
    paddle_l_y = paddle_l.ycor()
    if abs(ball_y - paddle_r_y) < 50 and abs(ball_x - paddle_r_x) < 10:
        ball.bounce()
        ball.forward(21)
        MOVE_DISTANCE += 0.2
    if abs(ball_y - paddle_l_y) < 50 and abs(ball_x - paddle_l_x) < 10:
        ball.bounce()
        ball.forward(21)
        MOVE_DISTANCE += 0.2
    if ball.ycor() > 300:
        ball.border_bounce()
    if ball.ycor() < -300:
        ball.border_bounce()
    if ball.xcor() < -350:
        scoreboard_r.increase_score()
        ball.reset_ball_l()
        MOVE_DISTANCE = 1
    if ball.xcor() > 350:
        scoreboard_l.increase_score()
        ball.reset_ball_r()
        MOVE_DISTANCE = 1

    if scoreboard_r.score == 10 or scoreboard_l == 10:
        scoreboard.game_over()
        game_going = False

screen.exitonclick()
