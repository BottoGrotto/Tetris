from shapes import Shape
class I(Shape):
    def __init__(self, row, col):
        self.id = 1
        self.color = (16, 230, 219)
        self.shape = [(0, 0), 
                        (0, 1), 
                        (0, 2), 
                        (0, 3)]
        self.row = row
        self.col = col