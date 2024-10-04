from pieces import Pieces
class I(Pieces):
        def __init__(self):
            self.id = 1
            self.color = (7, 224, 240)
            self.pos = [0, 3]
            self.shape = [(0, 0), (0, 1), (0, 2), (0, 3)]
            self.shapeNormal = [(0, 0), (0, 1), (0, 2), (0, 3)]
            self.shapeRotated = [(0, 0), 
                                 (1, 0), 
                                 (2, 0), 
                                 (3, 0)]
            self.rotated = False
            self.landed = False

        
