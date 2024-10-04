from shapes import Shape
class O(Shape):
        def __init__(self, row, col):
            self.id = 2
            self.color = (237, 240, 58)
            self.shape = [(0, 0), (0, 1),
                          (1, 0), (1, 1)]
            
            self.row = row
            self.col = col