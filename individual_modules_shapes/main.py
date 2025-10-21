from individual_modules_shapes import Point, Rectangle, Square, TriangleEquilateral, TriangleIsosceles, TriangleScalene, TriangleRectangle

def main():
    point_1 = Point(0.0, 0.0)
    point_2 = Point(5.0, 5.0)
    point_3 = Point(5.0, 2.0)
    
    'RECTANGLE AND SQUARE'
    rectangle = Rectangle(point_1, point_3)
    area_rectangle = rectangle.compute_area()
    perimeter_rectangle = rectangle.compute_perimeter()
    angles_rectangle = rectangle.compute_inner_angles()
    nature_shape_rectangle = rectangle.is_it_regular()
    print(f"""calculating that involve to rectangle
            are: {area_rectangle} <-- area,
            {perimeter_rectangle} <-- perimeter
            {angles_rectangle} <-- angles,
            {nature_shape_rectangle} <-- nature shape""")
    
    square = Square(point_1, point_2)
    area_square = square.compute_area()
    perimeter_square = square.compute_perimeter()
    angles_square = square.compute_inner_angles()
    nature_shape_square = square.is_it_regular()
    print(f"""calculating that involve to square
            are: {area_square} <-- area,
            {perimeter_square} <-- perimeter
            {angles_square} <-- angles,
            {nature_shape_square} <-- nature shape""")
    
    "TRIANGLE EQUILATERAL"
    point_A = Point(0.0, 0.0)
    point_B = Point(4.0, 0.0)
    point_C = Point(2.0, 3.4641016151377544)

    triangle_equilateral = TriangleEquilateral(point_A, point_B, point_C)
    area_triangle_equilateral = triangle_equilateral.compute_area()
    perimeter_triangle_equilateral = triangle_equilateral.compute_perimeter()
    angles_triangle_equilateral = triangle_equilateral.compute_inner_angles()
    nature_shape_triangle_equilateral = triangle_equilateral.is_it_regular()
    print(f"""calculating that involve to equilateral triangle
            are: {area_triangle_equilateral} <-- area,
            {perimeter_triangle_equilateral} <-- perimeter
            {angles_triangle_equilateral} <-- angles,
            {nature_shape_triangle_equilateral} <-- nature shape""")
    
    "TRIANGLE ISOSCELES"
    point_D = Point(0.0, 0.0)
    point_E = Point(4.0, 0.0)
    point_F = Point(2.0, 3.0)
    triangle_isosceles = TriangleIsosceles(point_D, point_E, point_F)
    area_triangle_isosceles = triangle_isosceles.compute_area()
    perimeter_triangle_isosceles = triangle_isosceles.compute_perimeter()
    angles_triangle_isosceles = triangle_isosceles.compute_inner_angles()
    nature_shape_triangle_isosceles = triangle_isosceles.is_it_regular()
    print(f"""calculating that involve to isosceles triangle
            are: {area_triangle_isosceles} <-- area,    
            {perimeter_triangle_isosceles} <-- perimeter
            {angles_triangle_isosceles} <-- angles,
            {nature_shape_triangle_isosceles} <-- nature shape""")
    
    "TRIANGLE SCALENE"
    point_G = Point(0.0, 0.0)
    point_H = Point(4.0, 0.0)
    point_I = Point(3.0, 2.0)
    
    triangle_scalene = TriangleScalene(point_G, point_H, point_I)
    area_triangle_scalene = triangle_scalene.compute_area()
    perimeter_triangle_scalene = triangle_scalene.compute_perimeter()
    angles_triangle_scalene = triangle_scalene.compute_inner_angles()
    nature_shape_triangle_scalene = triangle_scalene.is_it_regular()
    print(f"""calculating that involve to scalene triangle
            are: {area_triangle_scalene} <-- area,
            {perimeter_triangle_scalene} <-- perimeter
            {angles_triangle_scalene} <-- angles,
            {nature_shape_triangle_scalene} <-- nature shape""")
    
    "TRIANGLE RECTANGLE"
    point_J = Point(0.0, 0.0)
    point_K = Point(4.0, 0.0)
    point_L = Point(0.0, 3.0)
    triangle_rectangle = TriangleRectangle(point_J, point_K, point_L)
    area_triangle_rectangle = triangle_rectangle.compute_area()
    perimeter_triangle_rectangle = triangle_rectangle.compute_perimeter()
    angles_triangle_rectangle = triangle_rectangle.compute_inner_angles()
    nature_shape_triangle_rectangle = triangle_rectangle.is_it_regular()
    print(f"""calculating that involve to right triangle
            are: {area_triangle_rectangle} <-- area,
            {perimeter_triangle_rectangle} <-- perimeter
            {angles_triangle_rectangle} <-- angles,
            {nature_shape_triangle_rectangle} <-- nature shape""")

if __name__ == "__main__":
    main()