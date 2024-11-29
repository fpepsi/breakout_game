from turtle import Turtle
from constants import GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT, PADDLE_WIDTH_FACTOR, PADDLE_HEIGHT_FACTOR

class Paddle(Turtle):
    def __init__(self, color, speed, shape):
        super().__init__()
        self.ht()
        self.shape('square')
        self.shapesize(PADDLE_HEIGHT_FACTOR, PADDLE_WIDTH_FACTOR)
        self.color(color)
        self.speed(speed)
        self.penup()
        self.goto(x=0, y=- GAME_SCREEN_HEIGHT / 2 + 20)
        self.st()

    def move_turtle(self, event):
        """Move the turtle to the mouse pointer's x position."""
        self.goto(event.x - GAME_SCREEN_WIDTH // 2, - GAME_SCREEN_HEIGHT / 2 + 20)



