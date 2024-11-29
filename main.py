from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import BrickSet
from score import ScoreBoard
from constants import GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT
import time


screen = Screen()
screen.bgcolor('black')
screen.title('Breakout Game')
# sets up game screen position and mouse coordinates' adjustment
comp_scr_width = screen.cv.winfo_screenwidth()
comp_scr_height = screen.cv.winfo_screenheight()
start_x = (comp_scr_width - GAME_SCREEN_WIDTH) // 2
start_y = (comp_scr_height - GAME_SCREEN_HEIGHT) // 2
screen.setup(width=GAME_SCREEN_WIDTH, height=GAME_SCREEN_HEIGHT, startx=start_x, starty=start_y)
screen.tracer(0)

# creates paddle
paddle = Paddle(color='green', speed='fastest', shape='square')
screen.cv.bind('<Motion>', paddle.move_turtle)
# creates ball
ball = Ball()
# create brick wall
bricks = BrickSet()
# create score
score = ScoreBoard()

def run_game():
    game_on = True
    ball.start_ball()
    while game_on and score.rounds > 0:
        ball.move()
        ball.test_wall_collision()
        ball.test_paddle_collision(paddle.xcor(), score)
        ball.test_brick_collision(bricks, score)
        if score.win == 1:
            game_on = False
        time.sleep(0.001)
        screen.update()

    if score.win:
        answer = screen.textinput('Congratulations, you won! Play again?', 'yes / no').strip().lower()
    else:
        answer = screen.textinput('Game Over! would you like to play again', 'yes / no').strip().lower()

    if answer and answer[0] == 'y':
        bricks.reset_screen()
        score.reset_score()
        screen.update()
        run_game()
    else:
        screen.bye()

run_game()
screen.exitonclick()
