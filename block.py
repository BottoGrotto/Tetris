import pygame

class Block:
    def __init__(self, size, pos, color):
        self.display = pygame.display.get_surface()
        self.size = size
        self.pos = pos
        self.color = color

    def draw(self):
        pygame.draw.rect(self.display, self.color, (self.pos[0], self.pos[1], self.pos[0] + self.size, self.pos[1] + self.size))