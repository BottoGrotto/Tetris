from pieces import Pieces
class L(Pieces):
        def __init__(self):
            self.shape = [(0, 0), 
                                (1, 0), 
                                (2, 0), (2, 1)]
            super().__init__(self.shape)
            self.id = 3
            self.color = (240, 221, 12)
            self.pos = [3, 3]
            
            self.shapeNormal = [(0, 0), 
                                (1, 0), 
                                (2, 0), (2, 1)]
            self.shapeRotated = [(0, 0), (0, 1), (0, 2), (-1, 2)]
            self.rotated = False
            self.landed = False