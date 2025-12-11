Geometry Shapes with Python Decorators reto - 7

# Overview
Extension of the geometry shapes system from Challenge #5, now enhanced with Python decorators to demonstrate advanced OOP concepts.

# Added Decorators

## 1. @property Decorators
All protected attributes are now accessible through properties:

- shape.vertices - Returns tuple of vertices
- shape.edges - Returns tuple of edges
- shape.shape_type - Returns class name
- shape.num_vertices - Returns vertex count
- shape.num_edges - Returns edge count

## 2. @classmethod Decorators
Factory methods for creating shapes:
- New alternative to constructor
  - Rectangle.from_points(p1, p2)
  - Square.from_points(p1, p2) 
  - TriangleEquilateral.from_points(p1, p2, p3)
  - TriangleIsosceles.from_points(p1, p2, p3)
  - TriangleScalene.from_points(p1, p2, p3)
  - TriangleRectangle.from_points(p1, p2, p3)

## 3. Custom @time_execution Decorator
Measures execution time of computational methods:
- Applied to compute_area(), compute_perimeter(), 
- Automatically prints: "compute_area executed in 0.000012 seconds"
- Located in shape.py as a standalone decorator function

# File Structure
- shape.py - Base class with all decorators
- rectangle.py - Rectangle/Square with classmethods
- triangle.py - Triangle subclasses with classmethods
- point_line.py - Point and Line classes
- main.py - Updated to use classmethods

Note: This extends the existing Challenge #5 code without breaking original functionality.