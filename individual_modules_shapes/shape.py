from .point_line import Point, Line

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