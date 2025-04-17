class Color:
    def __init__(self, color):
        self.color = color

    def __sub__(self, other):
        if isinstance(other, int):
            tmp_color = self.color.copy()
            for i, val in enumerate(self.color):
                if val != 0 and val - other >= 0:
                    tmp_color[i] = val - other
        return tuple(tmp_color)
    
    def colorize(self):
        return tuple(self.color)
    # def __repr__(self):
    #     pass
        