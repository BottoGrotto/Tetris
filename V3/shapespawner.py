import pygame, random
from shape import Square, L_1, L_2, T, I, Z_1, Z_2
from timer import Timer
from color import Color

class ShapeSpawner:
    def __init__(self):
        self.options = [Square, L_1, L_2, T, I, Z_1, Z_2]
        self.colors = [Color([255, 0, 0]), Color([0, 255, 0]), Color([0, 0, 255]), Color([0, 255, 255]), Color([255, 255, 0]), Color([255, 0, 255]), Color([255, 180, 0])]
        self.spawn_timer = Timer(2000)
        self.spawn_timer.start(loop=True)
        # self.shape_to_spawn = self.random_shape()

    def random_shape(self):
        return self.options[random.randint(0, len(self.options) - 1)]()
    