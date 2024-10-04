import pygame, sys, math, random
from timer import Timer
from I import I
from O import O
from L import L

class Tetris:
    def __init__(self, size: tuple, boxSize):
        self.size = size
        self.boxSize = boxSize

        self.rows = math.floor((size[1] - 60)/boxSize)
        self.cols = math.floor(size[0]/boxSize)

        self.display = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        self.duration = 250

        self.timers = {0: Timer(self.duration),
                       1: Timer(25)}

        self.map = self.create_map()

        self.I = I
        self.O = O
        self.L = L

        self.shapes = []
        self.spawn_shape()

        self.moveDirection = 0
        self.rotateBool = False
        self.drop = False
        

    def create_map(self): 
        arr = list(range(0, self.rows))
        for i, row in enumerate(arr):
            arr[i] = (list(range(0, self.cols)))
            for j, col in enumerate(arr[i]):
                arr[i][j] = 0
                # print(i, j, print(arr[i][j]))
        # print(f"Rows(i): {len(arr)} || Cols(j): {len(arr[0])}")
        # print(arr)
        return arr
    
    def draw_board(self):
        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                x = j * self.boxSize
                y = i * self.boxSize
                if self.map[i][j] == 0:
                    pygame.draw.rect(self.display, (24, 24, 24), ((x, y), (self.boxSize, self.boxSize)), width= 1)
                if self.map[i][j] == 1:
                    pygame.draw.rect(self.display, self.I().color, ((x, y), (self.boxSize, self.boxSize)), width= 1)
                if self.map[i][j] == 2:
                     pygame.draw.rect(self.display, self.O().color, ((x, y), (self.boxSize, self.boxSize)), width= 1)
                if self.map[i][j] == 3:
                     pygame.draw.rect(self.display, self.L().color, ((x, y), (self.boxSize, self.boxSize)), width= 1)

    def spawn_shape(self):
        # randomPiece = random.randint(0, 1)
        randomPiece = 2
        if randomPiece == 0:
            piece = self.I()
        elif randomPiece == 1:
            piece = self.O()
        elif randomPiece == 2:
            piece = self.L()
        self.shapes.append(piece)
        for quard in piece.shape:
            self.map[piece.pos[0] + quard[0]][piece.pos[1] + quard[1]] = piece.id
        self.timers[0].start()

    def update_map(self):
        self.map = self.create_map()
        for piece in self.shapes:
            for quard in piece.shape:
                self.map[piece.pos[0] + quard[0]][piece.pos[1] + quard[1]] = piece.id




    def run(self):
        while True:
            if not self.timers[0].running:
                self.moveDirection = 0
            self.clock.tick(60)
            # keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.moveDirection = -1
                        print("left")
                    elif event.key == pygame.K_d:
                        self.moveDirection = 1
                        print("right")

                    if event.key == pygame.K_w:
                        self.rotateBool = True
                    elif event.key == pygame.K_s:
                        self.drop = True
                        self.duration = 50
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        self.drop = False
                        self.duration = 250
                        
            self.display.fill("black")
            self.draw_board()

            for timer in self.timers:
                self.timers[timer].update()
            
            

            if not self.timers[0].running:
                for piece in self.shapes:
                    if not piece.landed:
                        piece.move_down(self.map)
                        if piece.landed:
                            self.spawn_shape()
                            
                self.timers[0].start()
                # print(self.moveDirection)
                self.update_map()

            if not self.timers[1].running:
                # print("Movding")
                pieceToMove = self.shapes[-1]
                pieceToMove.move_side(self.map, self.moveDirection)
                if not pieceToMove.landed:
                    self.timers[1].start()
                
                self.moveDirection = 0

                if self.rotateBool:
                    pieceToMove.rotate(self.map)
                    self.rotateBool = False

                self.update_map()
            
            if self.drop:
                pieceToMove = self.shapes[-1]
                pieceToMove.move_side(self.map, self.moveDirection)
                if not pieceToMove.landed:
                    self.timers[0].duration = self.duration
                # self.drop = False
            else:
                self.timers[0].duration = self.duration
                

                

            











            # mousePos = pygame.mouse.get_pos()
            # mouseRow = math.floor(mousePos[1]/self.boxSize)
            # mouseCol = math.floor(mousePos[0]/self.boxSize)

            # print(mouseRow, mouseCol)
            pygame.display.update()

if __name__ == "__main__":
    game = Tetris((400, 700), 40)
    game.run()