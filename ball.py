from constants import *
from turtle import Turtle
from random import randint
import numpy as np
from constants import BALL_INITIAL_SPEED


class Ball(Turtle):
    ''' creates and manages the game ball'''
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.step = 5
        self.speed(BALL_INITIAL_SPEED)

    def start_ball(self):
        '''initializes the ball movement on a random direction'''
        # ball initializes from mid bottom
        x = randint(- GAME_SCREEN_WIDTH // 4, GAME_SCREEN_WIDTH // 4)
        y = - GAME_SCREEN_HEIGHT / 2 + 40
        if x < 0:
            self.setheading(randint(30, 60))
        elif x > 0:
            self.setheading(randint(120, 150))
        self.goto(x, y)
        self.showturtle()

    def move(self):
        self.forward(self.step)


    def test_wall_collision(self):
        if self.xcor() <= - GAME_SCREEN_WIDTH // 2 + 10 or self.xcor() >= GAME_SCREEN_WIDTH // 2 - 20:
            self.ball_reflect_vertical()
        elif self.ycor() >= GAME_SCREEN_HEIGHT // 2 - 10:
            self.ball_reflect_horizontal()


    def test_paddle_collision(self, x_cor, score):
        ''' test if ball within paddle boundaries'''
        if self.ycor() >= - GAME_SCREEN_HEIGHT // 2 + 60:
            pass
        elif self.ycor() < - GAME_SCREEN_HEIGHT // 2:
            score.rounds -= 1
            score.update_balls()
            if score.rounds > 0:
                self.start_ball()
        else:
            left_x = x_cor - PADDLE_WIDTH_FACTOR * 10
            right_x = x_cor + PADDLE_WIDTH_FACTOR * 10
            ball_heading = self.heading()
            if left_x <= self.xcor() <= right_x and 180 < ball_heading < 360:
                self.ball_reflect_horizontal()


    def test_brick_collision(self, bricks: object, score: object):
        ''' check if ball coordinates hit the bottom or the side of a brick'''
        # filter the array and return list of bricks which overlap the ball's current coordinates
        # filter by rows
        filtered_xcor = [brick for row in bricks.brick_set for brick in row if brick
                         and (brick.xcor() - 40) < self.xcor() < (brick.xcor() + 40)]
        # filter by columns
        if len(filtered_xcor) > 0:
            filtered_brick = [brick for brick in filtered_xcor if (brick.ycor() - 10) < self.ycor() < (brick.ycor() + 10)]
            if filtered_brick: # brick detected
                # logic below determines if the brick was hit on the sides or top/bottom, determining the escape angle
                for brick in filtered_brick:
                    brick.ht()
                    indices = np.where(bricks.brick_set == brick) # find the array position of brick being hit
                    row, col = indices[0][0], indices[1][0]
                    # test if brick was hit laterally
                    if col > 0 and bricks.brick_set[row, col - 1]:
                        brick_left = True
                    else:
                        brick_left = False
                    if col < 13 and bricks.brick_set[row, col + 1]:
                        brick_right = True
                    else:
                        brick_right = False
                    if (self.xcor() - 10 < brick.xcor() - 40 and not brick_left
                            or self.xcor() + 10 > brick.xcor() + 40 and not brick_right):
                        self.ball_reflect_vertical()
                    else:
                        self.ball_reflect_horizontal()

                    score.score += brick.points
                    score.update_scoreboard()

                    # after reflecting the ball, adjust brickset, score, ball speed, and test if any bricks left
                    orange_count = sum(1 for brick in bricks.brick_set.flat if brick and brick.pencolor() == 'orange')
                    if brick.pencolor() == 'orange' and orange_count == 28:
                        self.speed(BALL_INITIAL_SPEED + 5)
                        self.step +=5
                    red_count = sum(1 for brick in bricks.brick_set.flat if brick and brick.pencolor() == 'red')
                    if brick.pencolor() == 'red' and red_count == 28:
                        self.speed(BALL_INITIAL_SPEED + 6)
                        self.step += 5

                    # removes brick from wall
                    bricks.brick_set[row, col] = None

                    # test for last brick (game over) and ball speed increases for hits 4 and 12
                    none_count = sum(1 for brick in bricks.brick_set.flat if not brick)
                    if none_count == BRICK_ROWS * BRICK_COLS:
                        score.win = 1
                    elif none_count == 4:
                        self.speed(BALL_INITIAL_SPEED + 2)
                    elif none_count == 12:
                        self.speed(BALL_INITIAL_SPEED + 4)


            else:
                # no brick in the y-range covered by the turtle
                pass
        else:
            # no brick in the x-range covered by the turtle
            pass


    def ball_reflect_horizontal(self):
        self.setheading(360 - self.heading())


    def ball_reflect_vertical(self):
        self.setheading(180 - self.heading())




