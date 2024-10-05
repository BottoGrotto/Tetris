import pygame

class Pieces:
    def __init__(self, shape):
        self.rotationMatrix = [[0, -1],
                                [1, 0]]

        self.rotation = 0
        self.pre = shape
    
    def move_down(self, map):
            if not self.checkCollisionBottom(map):
                self.pos[0] += 1
            else:
                self.landed = True

    def move_side(self, map, dir):
        if dir == -1 and self.pos[1] - 1 >= 0:
            self.pos[1] -= 1
        elif dir == 1 and self.pos[1] + 1 <= len(map[0]) - 1:
            self.pos[1] += 1


    def checkCollisionSides(self, map, moveDirection=0):
        """Returns True if collision False if no collision"""
        # hit = False
        
        for quard in self.shape:
            row = self.pos[0] + quard[0]
            col = self.pos[1] + quard[1] + moveDirection

            if col >= 0 and col <= len(map[0])-1:
                print(col)
                sideState = map[row][col]

                hittingItSelf = self.checkPos(row, col)

                if sideState != 0 and not hittingItSelf:
                    # print("not hitting itself")
                    return True

            else:
                return True
        return False

    def checkCollisionBottom(self, map):
        """Returns True if collision False if no collision"""
        # hit = False
        for quard in self.shape:
            row = self.pos[0] + quard[0] + 1
            col = self.pos[1] + quard[1]
            # if topOrSide == "side":
            #     if col < 0:
            #         print("Hey yo", col)
            #         return True
            #     return True
            # print(row, col)
            if row <= len(map) -1:
                # if col > 0 :
                #     leftState = map[]
                belowState = map[row][col]
                
                hittingItSelf = self.checkPos(row, col)

                if belowState != 0 and not hittingItSelf:
                    # print("not hitting itself")
                    return True

            else:
                return True
        return False
            
    def checkPos(self, row, col):
        for quard in self.shape:
            if row == self.pos[0] + quard[0] and col == self.pos[1] + quard[1]:
                return True
        return False
    
    def rotate(self, map):

        if self.rotation == 0:
            self.shape = self.shapeNormal
            # self.rotated = False
            # self.pos[1] -= 1
        else:
            # self.rotation += 1
            
            # self.shape = self.shapeRotated
            # self.rotated = True
            self.pre = self.shape
            self.applyRotationMatrix()
            self.shape = self.shapeRotated
            # self.pos[1] += 1
            if self.rotation > 3:
                self.shape = self.shapeNormal
                self.rotation = 0
                # self.pos[1] -= 1
            print(self.rotation)

    def rotateCheck(self, map):
        if self.checkCollisionSides(map):
            print("cant rotate")
            self.shape = self.pre
            # self.rotated = False
            # self.pos[1] -= 1
            self.rotation -= 1
            return False
        return True

    def applyRotationMatrix(self):
        print(self.shape)
        for i, quard in enumerate(self.shape):
            # newQuard = []
            x = quard[0] * self.rotationMatrix[0][0] + quard[1] * self.rotationMatrix[0][1]
            y = quard[0] * self.rotationMatrix[1][0] + quard[1] * self.rotationMatrix[1][1]
            # newQuard.append(x, y)
            self.shapeRotated[i] = [x, y]

        

        print(self.shapeRotated)


