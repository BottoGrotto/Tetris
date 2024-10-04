import pygame

class Block:
    def __init__(self, size):
        self.display = pygame.display.get_surface()
        self.size = size

    def draw(self, color, x, y):
        pygame.draw.rect(self.display, color, (x, y, x + self.size, y + self.size))
        # pygame.draw.rect(self.display, color, (x+1, y+1, x-1 + self.size, y-1 + self.size))