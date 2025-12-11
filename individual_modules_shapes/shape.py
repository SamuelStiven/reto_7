from .point_line import Point, Line
import time
from functools import wraps

def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.6f} segundos")
        return result
    return wrapper

class Shape:
    def __init__(self, vertices: list, edges: list):
        self._vertices: list[Point] = vertices
        self._edges: list[Line] = edges
        self._shape_type = self.__class__.__name__
    
    @property
    def vertices(self):
        return tuple(self._vertices)

    @property
    def edges(self):
        return tuple(self._edges) 
    
    @property
    def shape_type(self):
        return self._shape_type 
    
    @property
    def num_vertices(self):
        return len(self._vertices)
    
    @property
    def num_edges(self):
        return len(self._edges) 
    
    @classmethod
    def from_points(cls, *points):
        # Class method for creating shapes from points
        raise NotImplementedError('Shapes have to implement it')  
    
    @time_execution        
    def compute_area(self):
        raise NotImplementedError('Shapes have to implement it')
    
    @time_execution
    def compute_perimeter(self):
        raise NotImplementedError('Shapes have to implement it')
    
    @time_execution
    def compute_inner_angles(self):
        raise NotImplementedError('Shapes have to implement it')