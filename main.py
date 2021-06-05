from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    scoreboard.update_score()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect colision with wall
    if ball.ycor() > 285 or ball.ycor() < -275:
        ball.wall_bounce()

    #Detect colision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    #Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect when left paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()


    if scoreboard.l_point == 7 or scoreboard.r_point == 7:
        game_is_on = False

screen.exitonclick()