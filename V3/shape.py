import pygame
from pygame import Vector2 as vec2
from timer import Timer

class Shape:
    def __init__(self, id):
        self.id = id
        self.shape = None
        self.pos = vec2(4, 0)
        self.falling = True
        self.falling_speed = Timer(250)
        
        self.move_speed = Timer(75)
        self.move_speed.start(loop=True)

        self.can_rotate = True
        self.allowed_to_rotate = True
        

    def rotate(self, grid):
        tmp_shape = self.shape.copy()
        for i, pos in enumerate(tmp_shape):
            tmp_shape[i] = pos.rotate(90)
        
        for pos in tmp_shape:
            x = int(pos.x + self.pos.x)
            y = int(pos.y + self.pos.y)
            if pos.x + self.pos.x < 0 or pos.x + self.pos.x >= len(grid[0]) or pos.y + self.pos.y < 0 or pos.y + self.pos.y >= len(grid) or ((grid[y][x] == self.id or grid[y][x] != self.id and grid[y][x] != 0) and vec2(y, x) not in self.shape):
                return False
            
        self.shape = tmp_shape

        self.sort()

    def sorted(self):
        last_pos = self.shape[0]
        for pos in self.shape:
            if pos.y < last_pos.y:
                return False
            last_pos = pos
        return True
    
    def sort(self):
        while not self.sorted():
            for i, pos1 in enumerate(self.shape):
                for j, pos2 in enumerate(self.shape):
                    if pos1 == pos2:
                        continue
                    if pos1.y < pos2.y:
                        tmp = self.shape[i]
                        self.shape[i] = self.shape[j]
                        self.shape[j] = tmp
                       

    def input(self, grid):
        self.falling_speed.duration = 250
        keys = pygame.key.get_pressed()
        if self.move_speed.has_expired():
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.move(grid, -1)
                self.falling_speed.duration = 600
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.move(grid, 1)
                self.falling_speed.duration = 600
        
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.allowed_to_rotate:
            if self.can_rotate:
                self.rotate(grid)
                self.can_rotate = False

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.falling_speed.duration = 100

    def move(self, grid, direction):
        if self.falling:
            if not self.check_collision_sides(grid, direction):
                self.pos.x += direction

    def check_collision_sides(self, grid, direction):
        for pos in self.shape:
            x = int(self.pos.x + pos.x) + direction
            y = int(self.pos.y + pos.y)
            if x < 0 or x >= len(grid[0]) or ((grid[y][x] == self.id and vec2(y, x) not in self.shape) if x < len(grid[0]) else False) or (grid[y][x] != self.id and vec2(y, x) not in self.shape and grid[y][x] != 0) if x <= len(grid[0]) else False:
                return True
        return False

    def check_collision_down(self, grid):
        for pos in self.shape:
            x = int(self.pos.x + pos.x)
            y = int(self.pos.y + pos.y) + 1
            if y >= len(grid) or ((grid[y][x] == self.id and vec2(y, x) not in self.shape) if y < len(grid) else False) or (grid[y][x] != self.id and vec2(y, x) not in self.shape and grid[y][x] != 0) if y <= len(grid) else False:
                return True
        return False
    
    def remove_from_shapes(self, shapes):
        shapes.remove(self)
        return shapes
    
    def draw(self, grid):
        for pos in self.shape:
            x = int(self.pos.x + pos.x)
            y = int(self.pos.y + pos.y)
            grid[y][x] = self.id
        return grid

    def update(self, grid):
        self.input(grid)
        if self.falling and self.falling_speed.has_expired():
            if self.check_collision_down(grid):
                self.falling = False
            else:
                self.pos.y += 1
        
        return self.draw(grid)
                


class Square(Shape):
    def __init__(self):
        super().__init__(1)
        self.shape = [vec2(0, 0), vec2(1, 0), vec2(0, 1), vec2(1, 1)]
        self.allowed_to_rotate = False

class L_1(Shape):
    def __init__(self):
        super().__init__(2)
        self.shape = [vec2(-1, 0), vec2(0, 0), vec2(1, 0), vec2(1, 1)]
        self.sort()

class L_2(Shape):
    def __init__(self):
        super().__init__(3)
        self.shape = [vec2(-1, 0), vec2(0, 0), vec2(1, 0), vec2(-1, 1)]
        self.sort()

class T(Shape):
    def __init__(self):
        super().__init__(4)
        self.shape = [vec2(0, 0), vec2(0, 1), vec2(1, 0), vec2(-1, 0)]
        self.sort()

class I(Shape):
    def __init__(self):
        super().__init__(5)
        self.shape = [vec2(-1, 0), vec2(0, 0), vec2(1, 0), vec2(2, 0)]
        self.sort()

class Z_1(Shape):
    def __init__(self):
        super().__init__(6)
        self.shape = [vec2(-1, 0), vec2(0, 0), vec2(0, 1), vec2(1, 1)]
        self.sort()

class Z_2(Shape):
    def __init__(self):
        super().__init__(7)
        self.shape = [vec2(-1, 1), vec2(0, 0), vec2(0, 1), vec2(1, 0)]
        self.sort()



if __name__ == "__main__":
    sq = Square()
    print(sq.shape)
    sq.rotate()
    print(sq.shape)