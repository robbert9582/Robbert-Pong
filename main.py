from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

R_PADDLE_POS = (350, 0)
L_PADDLE_POS = (-350, 0)

# Load high score from file
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0

def save_high_score():
    with open("highscore.txt", "w") as file:
        file.write(str(high_score))

def display_high_score():
    scoreboard.update_scoreboard()

def close_program():
    scoreboard.save_high_score()
    screen.bye()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(R_PADDLE_POS)
l_paddle = Paddle(L_PADDLE_POS)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Bind the close_program function to the window closing event
screen._root.protocol("WM_DELETE_WINDOW", close_program)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (
        ball.distance(r_paddle) < 50 and ball.xcor() > 320
    ) or (
        ball.distance(l_paddle) < 50 and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect R paddle missed
    if ball.xcor() > 380:
        scoreboard.l_point()
        if scoreboard.l_jump_scare == 1:
            rand_gif_num = random.randint(1, 17)
            gif = fr"gifs\funny gif {rand_gif_num}.gif"
            screen.bgpic(picname=gif)
            screen.update()
            scoreboard.l_jump_scare = 0
            time.sleep(3)
            screen.bgpic(picname="nopic")
            screen.update()
        ball.reset_ball()
        r_paddle.reset_paddle(R_PADDLE_POS)
        l_paddle.reset_paddle(L_PADDLE_POS)
        screen.update()

    if ball.xcor() < -380:
        scoreboard.r_point()
        if scoreboard.r_jump_scare == 1:
            rand_gif_num = random.randint(1, 17)
            gif = fr"gifs\funny gif {rand_gif_num}.gif"
            screen.bgpic(picname=gif)
            screen.update()
            scoreboard.r_jump_scare = 0
            time.sleep(3)
            screen.bgpic(picname="nopic")
            screen.update()
        ball.reset_ball()
        r_paddle.reset_paddle(R_PADDLE_POS)
        l_paddle.reset_paddle(L_PADDLE_POS)
        screen.update()

    # Update high score
    if scoreboard.l_score > high_score or scoreboard.r_score > high_score:
        high_score = max(scoreboard.l_score, scoreboard.r_score)
        display_high_score()

# Save high score before exiting
save_high_score()
screen.bye()

