import pygame, sys, math
from block import Block

WIDTH = 400
HEIGHT = 700

BOXSIZE = 40

ROWS = math.floor(BOXSIZE/WIDTH)
COLS = math.floor(BOXSIZE/(HEIGHT - 60))

class Tetris:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.map = self.createBoard()
        self.block = Block(BOXSIZE, (0, 0), (0, 0, 255))
    
    def createBoard(self):
        arr = list(range(ROWS))
        for i, row in enumerate(arr):
            arr[i] = list(range(COLS))
            for j, col in enumerate(arr[i]):
                arr[i][j] = 0

    def run(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.display.fill("black")
            self.block.draw()
            pygame.display.update()

if __name__ == "__main__":
    game = Tetris()
    game.run()