from turtle import Turtle
from constants import GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT, BRICK_ROWS, BRICK_COLS
import numpy as np

class BrickSet():
    ''' creates the brick objects '''
    def __init__(self):
        self.brick_set = np.empty((BRICK_ROWS, BRICK_COLS), dtype=object)
        self.brick_sequence = ['red', 'orange', 'green', 'yellow']
        self.brick_points = {'yellow': 1, 'green': 3, 'orange': 5, 'red': 7}
        self.brick_shape = 'square'
        self.brick_shapesize = (1, 4)
        self.create_wall()


    def create_wall(self):
        '''organize bricks in the screen'''
        # creates brick walls and record respective coordinates
        for i in range(0, BRICK_ROWS):
            color = self.brick_sequence[i // 2]
            y_shift = 25
            for j in range(0, BRICK_COLS):
                new_brick = Turtle()
                new_brick.penup()
                new_brick.shape(self.brick_shape)
                new_brick.color(color)
                new_brick.shapesize(self.brick_shapesize[0], self.brick_shapesize[1])
                new_brick.points = self.brick_points[color]
                self.brick_set[i, j] = new_brick
                brick_coord = (-GAME_SCREEN_WIDTH // 2 + 42 + j * 85,
                               GAME_SCREEN_HEIGHT // 2 - 100 - i * y_shift)
                new_brick.setpos(brick_coord[0], brick_coord[1])


    def reset_screen(self):
        self.brick_set = np.empty((BRICK_ROWS, BRICK_COLS), dtype=object)
        self.create_wall()
