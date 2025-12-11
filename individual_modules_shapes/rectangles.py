from .shape import Shape
from .point_line import Point, Line

class Rectangle(Shape):
    def __init__(self, point1: 'Point', point2: 'Point'):
        x1, y1 = point1.x, point1.y
        x2, y2 = point2.x, point2.y
        
        bottom_left = Point(min(x1, x2), min(y1, y2))
        bottom_right = Point(max(x1,x2), min(y1, y2))
        top_left = Point(min(x1,x2), max(y1,y2))
        top_right = Point(max(x1,x2), max(y1,y2))
        
        vertices = [bottom_left, bottom_right, top_left, top_right]
        
        edges = [Line(bottom_left, bottom_right),
                 Line(bottom_right, top_right),
                 Line(top_right, top_left),
                 Line(top_left, bottom_left)]
        
        super().__init__(vertices=vertices, edges=edges)
    
    @classmethod
    def from_points(cls, point1: 'Point', point2: 'Point'):
        # Create a rectangle from two opposite points
        return cls(point1, point2)
        
    def compute_area(self):
        return self._edges[0].length() * self._edges[1].length()
        
    def compute_perimeter(self):
        return sum(edge.length() for edge in self._edges)
        
    def compute_inner_angles(self):
        return "Inner angles of rectangle form are equivalent to 90°", 90, 90, 90, 90
       
    def is_it_regular(self):
        if self._edges[0].length() == self._edges[1].length():
            return True, "the rectangle is actually a square (regular shape)"
        else:
            return False, "it is a irregular shape"

class Square(Rectangle):
    def __init__(self, point1: 'Point', point2: 'Point'):
        super().__init__(point1, point2)
        if self._edges[0].length() != self._edges[1].length():
            raise ValueError("the points dont defines a square")
    @classmethod
    def from_points(cls, point1: 'Point', point2: 'Point'):
        # Create a square 
        return cls(point1, point2)