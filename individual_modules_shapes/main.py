from individual_modules_shapes import Point, Rectangle, Square, TriangleEquilateral, TriangleIsosceles, TriangleScalene, TriangleRectangle

def main():
    point_1 = Point(0.0, 0.0)
    point_2 = Point(5.0, 5.0)
    point_3 = Point(5.0, 2.0)
    
    # RECTANGLE AND SQUARE - Using @classmethod
    print("=" * 60)
    print("RECTANGLE AND SQUARE")
    print("=" * 60)
    
    # Using the classmethod from_points
    rectangle = Rectangle.from_points(point_1, point_3)
    area_rectangle = rectangle.compute_area()
    perimeter_rectangle = rectangle.compute_perimeter()
    angles_rectangle = rectangle.compute_inner_angles()
    nature_shape_rectangle = rectangle.is_it_regular()
    print(f"""Rectangle calculations:
            Area: {area_rectangle}
            Perimeter: {perimeter_rectangle}
            Angles: {angles_rectangle}
            Regular: {nature_shape_rectangle}""")
    
    # Using the classmethod from_points for Square
    square = Square.from_points(point_1, point_2)
    area_square = square.compute_area()
    perimeter_square = square.compute_perimeter()
    angles_square = square.compute_inner_angles()
    nature_shape_square = square.is_it_regular()
    print(f"""Square calculations:
            Area: {area_square}
            Perimeter: {perimeter_square}
            Angles: {angles_square}
            Regular: {nature_shape_square}""")
    
    # TRIANGLE EQUILATERAL - Using @classmethod
    print("\n" + "=" * 60)
    print("TRIANGLE EQUILATERAL")
    print("=" * 60)
    
    point_A = Point(0.0, 0.0)
    point_B = Point(4.0, 0.0)
    point_C = Point(2.0, 3.4641016151377544)

    # Using the classmethod from_points
    triangle_equilateral = TriangleEquilateral.from_points(point_A, point_B, point_C)
    area_triangle_equilateral = triangle_equilateral.compute_area()
    perimeter_triangle_equilateral = triangle_equilateral.compute_perimeter()
    angles_triangle_equilateral = triangle_equilateral.compute_inner_angles()
    nature_shape_triangle_equilateral = triangle_equilateral.is_it_regular()
    print(f"""Equilateral Triangle calculations:
            Area: {area_triangle_equilateral}
            Perimeter: {perimeter_triangle_equilateral}
            Angles: {angles_triangle_equilateral}
            Regular: {nature_shape_triangle_equilateral}""")
    
    # TRIANGLE ISOSCELES - Using @classmethod
    print("\n" + "=" * 60)
    print("TRIANGLE ISOSCELES")
    print("=" * 60)
    
    point_D = Point(0.0, 0.0)
    point_E = Point(4.0, 0.0)
    point_F = Point(2.0, 3.0)
    
    # Using the classmethod from_points
    triangle_isosceles = TriangleIsosceles.from_points(point_D, point_E, point_F)
    area_triangle_isosceles = triangle_isosceles.compute_area()
    perimeter_triangle_isosceles = triangle_isosceles.compute_perimeter()
    angles_triangle_isosceles = triangle_isosceles.compute_inner_angles()
    nature_shape_triangle_isosceles = triangle_isosceles.is_it_regular()
    print(f"""Isosceles Triangle calculations:
            Area: {area_triangle_isosceles}
            Perimeter: {perimeter_triangle_isosceles}
            Angles: {angles_triangle_isosceles}
            Regular: {nature_shape_triangle_isosceles}""")
    
    # TRIANGLE SCALENE - Using @classmethod
    print("\n" + "=" * 60)
    print("TRIANGLE SCALENE")
    print("=" * 60)
    
    point_G = Point(0.0, 0.0)
    point_H = Point(4.0, 0.0)
    point_I = Point(3.0, 2.0)
    
    # Using the classmethod from_points
    triangle_scalene = TriangleScalene.from_points(point_G, point_H, point_I)
    area_triangle_scalene = triangle_scalene.compute_area()
    perimeter_triangle_scalene = triangle_scalene.compute_perimeter()
    angles_triangle_scalene = triangle_scalene.compute_inner_angles()
    nature_shape_triangle_scalene = triangle_scalene.is_it_regular()
    print(f"""Scalene Triangle calculations:
            Area: {area_triangle_scalene}
            Perimeter: {perimeter_triangle_scalene}
            Angles: {angles_triangle_scalene}
            Regular: {nature_shape_triangle_scalene}""")
    
    # TRIANGLE RECTANGLE - Using @classmethod
    print("\n" + "=" * 60)
    print("TRIANGLE RECTANGLE (RIGHT TRIANGLE)")
    print("=" * 60)
    
    point_J = Point(0.0, 0.0)
    point_K = Point(4.0, 0.0)
    point_L = Point(0.0, 3.0)
    
    # Using the classmethod from_points
    triangle_rectangle = TriangleRectangle.from_points(point_J, point_K, point_L)
    area_triangle_rectangle = triangle_rectangle.compute_area()
    perimeter_triangle_rectangle = triangle_rectangle.compute_perimeter()
    angles_triangle_rectangle = triangle_rectangle.compute_inner_angles()
    nature_shape_triangle_rectangle = triangle_rectangle.is_it_regular()
    print(f"""Right Triangle calculations:
            Area: {area_triangle_rectangle}
            Perimeter: {perimeter_triangle_rectangle}
            Angles: {angles_triangle_rectangle}
            Regular: {nature_shape_triangle_rectangle}""")
    
    # Testing properties from Shape class
    print("\n" + "=" * 60)
    print("TESTING SHAPE PROPERTIES")
    print("=" * 60)
    
    print(f"Rectangle properties:")
    print(f"  Type: {rectangle.shape_type}")
    print(f"  Number of vertices: {rectangle.num_vertices}")
    print(f"  Number of edges: {rectangle.num_edges}")
    
    print(f"\nSquare properties:")
    print(f"  Type: {square.shape_type}")
    print(f"  Number of vertices: {square.num_vertices}")
    print(f"  Number of edges: {square.num_edges}")

if __name__ == "__main__":
    main()