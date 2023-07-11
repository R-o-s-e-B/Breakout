import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import Blocks
import random
from levels import *
from scoreboard import Score

block_list = []
colors = ["#4D455D", "#E96479", "#F5E9CF", "#7DB9B6", "#262A56", "#41644A"]
score = Score()

Y = -240
X = 0
pos = (0, -240)
ball_pos = (0, -220)

Window = Screen()



def game_three():
    Window.clear()
    global run
    Window.tracer(0)
    Window.setup(width=800, height=680)
    Window.title("Breakout")
    Window.listen()

    def genearate(level):
        for i in level:
            blocks = Blocks(i, random.choice(colors))
            block_list.append(blocks)

    genearate(level_three)

    paddle = Paddle(pos)
    ball = Ball(ball_pos)
    run = True
    while run:
        Window.update()
        time.sleep(ball.speed)
        Window.onkeypress(paddle.go_left, "a")
        Window.onkeypress(paddle.go_right, "d")
        paddle.check()

        ball.move()

        if ball.ycor() > 340 or ball.distance(paddle) < 40:
            ball.bounce_y()

        if ball.xcor() > 360 or ball.xcor() < -360:
            ball.bounce_x()

        if ball.ycor() < -380:
            score.lose_life()
            ball.reset_pos()

        for i in block_list:
            if ball.distance(i) < 20:
                if block_list != []:
                    block_list.remove(i)
                    i.hideturtle()
                if block_list == []:
                    run = False
                    Window.clear()
                    score.level_won()
                    time.sleep(3)
                    run = False


                score.score_points()
                score.update_score()

        if score.lives == 0:
            Window.clear()
            score.game_over()
            time.sleep(3)
            score.lives = 3
            score.clear()
            game()


def game_two():
    Window.clear()
    global run
    Window.tracer(0)
    Window.setup(width=800, height=680)
    Window.title("Breakout")
    Window.listen()

    def genearate(level):
        for i in level:
            blocks = Blocks(i, random.choice(colors))
            block_list.append(blocks)

    genearate(level_two)

    paddle = Paddle(pos)
    ball = Ball(ball_pos)
    run = True
    while run:
        Window.update()
        time.sleep(ball.speed)
        Window.onkeypress(paddle.go_left, "a")
        Window.onkeypress(paddle.go_right, "d")
        paddle.check()

        ball.move()

        if ball.ycor() > 340 or ball.distance(paddle) < 40:
            ball.bounce_y()

        if ball.xcor() > 360 or ball.xcor() < -360:
            ball.bounce_x()

        if ball.ycor() < -380:
            score.lose_life()
            ball.reset_pos()

        for i in block_list:
            if ball.distance(i) < 30:
                if block_list != []:
                    block_list.remove(i)
                    i.hideturtle()

                if block_list == []:

                    Window.clear()
                    score.level_three()
                    time.sleep(3)
                    run = False
                    game_three()
                score.score_points()
                score.update_score()



        if score.lives == 0:
            Window.clear()
            score.game_over()
            time.sleep(3)
            score.lives = 3
            score.clear()
            game()



def game():
    global run
    Window.tracer(0)
    Window.setup(width=800, height=680)
    Window.title("Breakout")
    Window.listen()

    def genearate(level):
        for i in level:
            blocks = Blocks(i, random.choice(colors))
            block_list.append(blocks)

    genearate(level_one)

    paddle = Paddle(pos)
    ball = Ball(ball_pos)
    run = True
    while run:
        Window.update()
        time.sleep(ball.speed)
        Window.onkeypress(paddle.go_left, "a")
        Window.onkeypress(paddle.go_right, "d")
        paddle.check()

        ball.move()

        if ball.ycor() > 340 or ball.distance(paddle) < 40:
            ball.bounce_y()

        if ball.xcor() > 360 or ball.xcor() < -360:
            ball.bounce_x()

        if ball.ycor() < -380:
            score.lose_life()
            ball.reset_pos()

        for i in block_list:
            if ball.distance(i) < 40:
                if block_list != []:
                    block_list.remove(i)
                    i.hideturtle()

                if block_list == []:
                    Window.clear()
                    score.level_two()
                    time.sleep(3)
                    run = False
                    game_two()
                score.score_points()
                score.update_score()



        if score.lives == 0:
            Window.clear()
            score.game_over()
            time.sleep(3)
            score.lives = 3
            score.clear()
            game()


game()



Window.exitonclick()

