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