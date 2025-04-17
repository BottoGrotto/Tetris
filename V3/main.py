import pygame, sys
from shapespawner import ShapeSpawner
pygame.mixer.init()
pygame.font.init()

BOX_SIZE = 40

class Game:
    def __init__(self, size):
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.size = size
        self.grid = self.make_grid()
        self.score = 0
        self.style = 4

        self.line_clear_sound = pygame.mixer.Sound("lineclear.mp3")

        self.spawner = ShapeSpawner()

        self.shapes = [self.spawner.random_shape()]
        self.shapes[-1].falling_speed.start(loop=True)
                   
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        
    def check_line_and_clear(self):
        clear_lines = []
        for i in range(len(self.grid)-1, -1, -1):
            line_len = 0
            for j in range(0, len(self.grid[0])):
                if self.grid[i][j] != 0:
                    line_len += 1
            if line_len == len(self.grid[0]):
                for j in range(0, len(self.grid[0])):
                    self.grid[i][j] = 0
                clear_lines.append(i)
            
        clear_lines.sort()
        for i, y_level in enumerate(clear_lines):
            self.shift_grid(y_level)

        if len(clear_lines) == 4:
            self.score += 1200
        elif len(clear_lines) == 3:
            self.score += 300
        elif len(clear_lines) == 2:
            self.score += 100
        elif len(clear_lines) == 1:
            self.score += 40

        if len(clear_lines) > 0:
            self.line_clear_sound.play()
  
    def shift_grid(self, y_level):
        for i in range(y_level, 0, -1):
            for j in range(0, len(self.grid[0])):
                tmp = self.grid[i-1][j]
                self.grid[i-1][j] = 0
                self.grid[i][j] = tmp

    def make_grid(self):
        arr = list(range(0, self.size[1] // BOX_SIZE))
        for i in range(len(arr)):
            arr[i] = list(range(0, self.size[0] // BOX_SIZE))
            for j in range(len(arr[i])):
                arr[i][j] = 0
        return arr
    
    def draw_boxes(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                id = self.grid[i][j]
                if id != 0:
                    pygame.draw.rect(self.screen, self.spawner.colors[id-1] - 75, ((j * BOX_SIZE, i * BOX_SIZE), (BOX_SIZE, BOX_SIZE)), width=self.style, border_radius=5)
                    pygame.draw.rect(self.screen, self.spawner.colors[id-1].colorize(), ((j * BOX_SIZE + self.style, i * BOX_SIZE + self.style), (BOX_SIZE-self.style, BOX_SIZE-self.style)), border_radius=5)

    def clear_grid(self):
        for shape in self.shapes:
             for pos in shape.shape:
                x = int(shape.pos.x + pos.x)
                y = int(shape.pos.y + pos.y)
                self.grid[y][x] = 0   
    
    def draw_grid(self):
        y = BOX_SIZE
        for i in range(len(self.grid)):
            pygame.draw.line(self.screen, (255, 255, 255), (0, y), (self.size[0], y), 1)
            y += BOX_SIZE

        x = BOX_SIZE
        for i in range(len(self.grid)):
            pygame.draw.line(self.screen, (255, 255, 255), (x, 0), (x, self.size[1]), 1)
            x += BOX_SIZE

    def draw_score(self):
        text_surface = self.font.render(f'{self.score}', True, (255, 255, 255))
        self.screen.blit(text_surface, (10,0))

    def run(self):
        while True:
            pygame.display.set_caption(f"Tetris  FPS: {int(self.clock.get_fps())}")
            self.screen.fill((0, 0, 0))
            self.clock.tick(60)
            self.draw_boxes()
            # self.draw_grid()
            self.clear_grid()
            self.check_line_and_clear()
            self.draw_score()


            if len(self.shapes) == 0:
                self.shapes.append(self.spawner.random_shape())
                self.shapes[-1].falling_speed.start(loop=True)
                
            for shape in self.shapes:
                shape.update(self.grid)
                if not shape.falling:
                    self.shapes.remove(shape)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        if self.style > 4:
                            self.style = 2
                        else:
                            self.style += 2
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if len(self.shapes) >= 1:
                            self.shapes[0].can_rotate = True

            pygame.display.update()

if __name__ == "__main__":
    Game((400, 800)).run()
