import pygame

class Pieces:
    # def __init__(self):
    #     self.I = I
    #     self.O = O  
    
    def move_down(self, map):
            if not self.checkCollision(map):
                self.pos[0] += 1
            else:
                self.landed = True

    def move_side(self, map, dir):
        if dir == -1 and self.pos[1] - 1 >= 0:
            self.pos[1] -= 1
        elif dir == 1 and self.pos[1] + 1 <= len(map[0]) - 1:
            self.pos[1] += 1


    def checkCollision(self, map):
        hit = False
        for quard in self.shape:
            row = self.pos[0] + quard[0] + 1
            col = self.pos[1] + quard[1]
            # print(row, col)
            if row <= len(map) -1:
                belowState = map[row][col]
                
                hittingItSelf = self.checkPos(row, col)

                if belowState != 0 and not hittingItSelf:
                    return True

            else:
                return True
        return hit
            
    def checkPos(self, row, col):
        for quard in self.shape:
            if row == self.pos[0] + quard[0] and col == self.pos[1] + quard[1]:
                return True
        return False
    
    def rotate(self, map):
        if self.rotated:
            self.shape = self.shapeNormal
            self.rotated = False
            self.pos[1] -= 1
        else:
            self.shape = self.shapeRotated
            self.rotated = True
            self.pos[1] += 1
            if self.checkCollision(map):
                print("cant rotate")
                self.shape = self.shapeNormal
                self.rotated = False
                self.pos[1] -= 1

        # print(self.shape)


