from math import acos, degrees

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    def computer_distance(self, point: 'Point') -> float:
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5

class Line:
    def __init__(self, start_point: 'Point', end_point: 'Point'):
        self._start_point = start_point
        self._end_point = end_point
    
    def length(self) -> float:
        return self._start_point.computer_distance(self._end_point)
    
    @property
    def start_point(self):
        return self._start_point

    @property
    def end_point(self):
        return self._end_point
        
class Shape:
    def __init__(self, vertices: list, edges: list):
        self._vertices: list[Point] = vertices
        self._edges: list[Line] = edges
    
    @property
    def vertices(self):
        return tuple(self._vertices)

    @property
    def edges(self):
        return tuple(self._edges)     
            
    def compute_area(self):
        raise NotImplementedError('Shapes have to implement it')
    
    def compute_perimeter(self):
        raise NotImplementedError('Shapes have to implement it')
    
    def compute_inner_angles(self):
        raise NotImplementedError('Shapes have to implement it')

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

class Triangle(Shape):
    def __init__(self, point1: 'Point', point2: 'Point', point3: 'Point'):
        vertices = [point1, point2, point3]
        edges = [Line(point1, point2), Line(point2, point3), Line(point3, point1)]
        super().__init__(vertices=vertices, edges=edges)

    def compute_perimeter(self):
        return sum(edge.length() for edge in self._edges)

class TriangleEquilateral(Triangle):
    def __init__(self, point1: 'Point', point2: 'Point', point3: 'Point'):
        super().__init__(point1, point2, point3)
        
        lengths = [edge.length() for edge in self._edges]
        
        if not (lengths[0] == lengths[1] == lengths[2]):
            raise ValueError("the points don't define an equilateral triangle")
    
    def compute_area(self):
        a = self._edges[0].length()
        area = (3**0.5 / 4) * a**2
        return area
    
    def compute_inner_angles(self):
        return "Inner angles of equilateral triangle form are equivalent to 60°", 60, 60, 60
    
    def is_it_regular(self):
        return True, "the triangle is a regular shape"

class TriangleIsosceles(Triangle):
    def __init__(self, point1: 'Point', point2: 'Point', point3: 'Point'):
        super().__init__(point1, point2, point3)
        
        lengths = [edge.length() for edge in self._edges]
        
        if not (lengths[0] == lengths[1] or lengths[1] == lengths[2] or lengths[0] == lengths[2]):
            raise ValueError("the points don't define an isosceles triangle")
        elif lengths[0] == lengths[1] == lengths[2]:
            raise ValueError("the points define an equilateral triangle, not an isosceles triangle")
        
    def compute_area(self):
        a = self._edges[0].length()
        b = self._edges[1].length()
        c = self._edges[2].length()
        
        if a == b:
            base = c
            side = a
        elif b == c:
            base = a
            side = b
        else:
            base = b
            side = a
        
        height = (side ** 2 - (base ** 2) / 4)**0.5
        area = (base * height) / 2
        return area
    
    def _calculate_angle(self, a: float, b: float, c: float) -> float:
        if a <= 0 or b <= 0:
            return 0.0
        cos_angle = (a*a + b*b - c*c) / (2*a*b)
        cos_angle = max(-1.0, min(1.0, cos_angle))  
        return degrees(acos(cos_angle))
    
    def compute_inner_angles(self):
        lengths = [edge.length() for edge in self._edges]
        
        if lengths[0] == lengths[1]:
            angle_vertex = self._calculate_angle(lengths[0], lengths[1], lengths[2])
            angle_base = (180 - angle_vertex) / 2
        elif lengths[1] == lengths[2]:
            angle_vertex = self._calculate_angle(lengths[1], lengths[2], lengths[0])
            angle_base = (180 - angle_vertex) / 2
        else:
            angle_vertex = self._calculate_angle(lengths[0], lengths[2], lengths[1])
            angle_base = (180 - angle_vertex) / 2
        return "Inner angles of isosceles triangle form are:", angle_vertex, angle_base, angle_base
    
    def is_it_regular(self):
        return False, "the triangle is an irregular shape"

class TriangleScalene(Triangle):
    def __init__(self, point1: 'Point', point2: 'Point', point3: 'Point'):
        super().__init__(point1, point2, point3)
        
        lengths = [edge.length() for edge in self._edges]
        
        if lengths[0] == lengths[1] or lengths[1] == lengths[2] or lengths[0] == lengths[2]:
            raise ValueError("the points don't define a scalene triangle")
    
    def compute_area(self):
        a = self._edges[0].length()
        b = self._edges[1].length()
        c = self._edges[2].length()
        
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        return area
    
    def _calculate_angle(self, a: float, b: float, c: float) -> float:
        if a <= 0 or b <= 0:
            return 0.0
        cos_angle = (a*a + b*b - c*c) / (2*a*b)
        cos_angle = max(-1.0, min(1.0, cos_angle))  
        return degrees(acos(cos_angle))
    
    def compute_inner_angles(self):
        lengths = [edge.length() for edge in self._edges]
        
        angle_A = self._calculate_angle(lengths[1], lengths[2], lengths[0])
        angle_B = self._calculate_angle(lengths[0], lengths[2], lengths[1])
        angle_C = self._calculate_angle(lengths[0], lengths[1], lengths[2])
        
        return "Inner angles of scalene triangle form are:", angle_A, angle_B, angle_C
    
    def is_it_regular(self):
        return False, "the triangle is an irregular shape"

class TriangleRectangle(Triangle):
    def __init__(self, point1: 'Point', point2: 'Point', point3: 'Point'):
        super().__init__(point1, point2, point3)
        
        lengths = [edge.length() for edge in self._edges]
        lengths.sort()
        
        if not (abs(lengths[0]**2 + lengths[1]**2 - lengths[2]**2) < 1e-9):
            raise ValueError("the points don't define a right triangle")
    
    def compute_area(self):
        lengths = [edge.length() for edge in self._edges]
        lengths.sort()
        
        a = lengths[0]
        b = lengths[1]
        
        area = (a * b) / 2
        return area
    
    def _calculate_angle(self, a: float, b: float, c: float) -> float:
        if a <= 0 or b <= 0:
            return 0.0
        cos_angle = (a*a + b*b - c*c) / (2*a*b)
        cos_angle = max(-1.0, min(1.0, cos_angle))  
        return degrees(acos(cos_angle))
    
    def compute_inner_angles(self):
        lengths = [edge.length() for edge in self._edges]
        lengths.sort()
        
        angle_A = self._calculate_angle(lengths[1], lengths[2], lengths[0])
        angle_B = self._calculate_angle(lengths[0], lengths[2], lengths[1])
        angle_C = 90.0
        
        return "Inner angles of right triangle form are:", angle_A, angle_B, angle_C
    
    def is_it_regular(self):
        return False, "the triangle is an irregular shape"