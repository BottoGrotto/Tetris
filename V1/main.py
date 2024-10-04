import pygame, sys, math
from block import Block
# from shapes import Shape
from I import I
from O import O

WIDTH = 400
HEIGHT = 700

BOXSIZE = 40

ROWS = math.floor(WIDTH/BOXSIZE)
COLS = math.floor((HEIGHT - 60)/BOXSIZE)
print(ROWS)
print(COLS)

class Tetris:
    def __init__(self):
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.map = self.create_board()
        self.block = Block(40)
        self.shapes = [O(4, 0)]
        self.i = I(3, 0)
        self.o = O(4, 0)
        for shape in self.shapes:
            self.map = shape.add_shape(self.map)
        # self.map = Shape.add_shape(self.o, self.map)
        # print(self.map)
        # self.map[0][0] = 1
        # self.map[1][1] = 1
        # self.map[3][9] = 1
        # print(len(self.map), len(self.map[len(self.map)-1]))
        # print(self.map)


    def create_board(self):
        # print(range(0, ROWS))
        arr = list(range(COLS))
        # print(arr)
        for i, col in enumerate(arr):
            arr[i] = list(range(ROWS))
            for j, row in enumerate(arr[i]):
                arr[i][j] = 0
        return arr

    def draw_board(self):
        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                x = j * BOXSIZE
                y = i * BOXSIZE
                
                state = self.map[i][j]

                if state > 0:
                    if state == 1:
                        self.block.draw(self.i.color , x, y)
                    if state == 2:
                        self.block.draw(self.o.color, x, y)
                else:
                    self.block.draw((24, 26, 25), x, y)

    def update_board(self):
        for shape in self.shapes:
            self.map = Shape.move(Shape, shape, self.map)
        # for i, row in enumerate(self.map):
        #     for j, col in enumerate(row):

        

    def run(self):
        
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.display.fill("black")
            self.draw_board()
            self.update_board()
            pygame.display.update()

if __name__ == "__main__":
    game = Tetris()
    game.run()