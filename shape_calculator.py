class Rectangle ():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        rectangleStr = "Rectangle(width=%d, height=%d)"%(self.width, self.height)
        return rectangleStr
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    
    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return "Too big for picture."
        else:
            row = "%s\n"%("*"*self.width)
            columns = row*self.height
            return columns        
    
    def get_amount_inside(self, shape):
        if self.width < shape.width:
            if self.height < shape.height:
                return 0
            else:
                return int(self.height / shape.height)   
        else:
            if self.height < shape.height:
                return int(self.width / shape.width)
            else:
                return int(self.width / shape.width) * int(self.height / shape.height)
        
class Square (Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        squareStr = "Square(side=%d)"%(self.width)
        return squareStr 
        
    def set_side(self, side):
        self.width = side
        self.height = side