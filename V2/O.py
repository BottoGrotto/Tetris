from pieces import Pieces
class O(Pieces):
        def __init__(self):
            self.shape = [(0, 0), (0, 1), 
                          (1, 0), (1, 1)]
            super().__init__(self.shape)
            self.id = 2
            self.color = (10, 25, 161)
            self.pos = [0, 2]
            
            self.shapeNormal = [(0, 0), (0, 1), 
                                (1, 0), (1, 1)]
            self.shapeRotated = [(0, 0), (0, 1), 
                                (1, 0), (1, 1)]
            self.rotated = False
            self.landed = False
            

        