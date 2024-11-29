from turtle import Turtle
from constants import SCORE_X, SCORE_Y, ROUNDS, BALLS_X, BALLS_Y

class ScoreBoard():
    def __init__(self):
        super().__init__()
        self.score = 0
        self.rounds = ROUNDS
        self.location_score = [SCORE_X, SCORE_Y]
        self.location_balls = [BALLS_X, BALLS_Y]
        self.create_score()
        self.create_balls()
        self.win = 0

    def create_score(self):
        ''' creates the screen score widget '''
        self.score_display = Turtle()
        self.score_display.hideturtle()
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.goto(self.location_score[0],self.location_score[1])
        self.score_display.write(f"Score = {self.score}", False, 'center', ('Helvetica', 28, 'normal'))


    def create_balls(self):
        ''' creates the screen ball count widget '''
        self.ball_display = Turtle()
        self.ball_display.hideturtle()
        self.ball_display.color("white")
        self.ball_display.penup()
        self.ball_display.goto(self.location_balls[0],self.location_balls[1])
        self.ball_display.write(f"Balls = {self.rounds}", False, 'center', ('Helvetica', 28, 'normal'))


    def update_scoreboard(self):
        self.score_display.clear()
        self.score_display.write(f"Score = {self.score}", False, 'center', ('Helvetica', 28, 'normal'))


    def update_balls(self):
        self.ball_display.clear()
        self.ball_display.write(f"Balls = {self.rounds}", False, 'center', ('Helvetica', 28, 'normal'))


    def reset_score(self):
        self.score = 0
        self.rounds = ROUNDS
        self.update_scoreboard()
        self.rounds = ROUNDS
        self.update_balls()