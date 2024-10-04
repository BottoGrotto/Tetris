from block import Block

class Shape:
    def add_shape(shape, map):
        for cube in shape.shape:
            map[shape.row + cube[0]][shape.col + cube[1]] = shape.id
        return map
    
    def remove_shape(self, shape, map):
        for cube in shape.shape:
            map[shape.row + cube[0]][shape.col + cube[1]] = 0
        return map
    
    def move(self, shape, map):
        if shape.row + 1 < len(map):
            map = self.remove_shape(self, shape, map)
            shape.row += 1
            for i, cube in enumerate(shape.shape):
                map[shape.row + cube[0]][shape.col + cube[1]] = shape.id
            return map
        else:
            return map
    
    
        
        # def move(self):
        #     self.row += 1
        
        # def update(self):

            
    
    