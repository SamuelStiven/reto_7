Geometric Shapes Packages - Reto 5

Description
Implementation of a geometric shapes system in Python, demonstrating two package organization approaches.

Project Structure

Option 1 - Single Module

module_shapes/
shapes.py: All classes in a single module

main.py: Test code for option 1

Option 2 - Separate Modules

individual_modules_shapes/

point_line.py: Point and Line classes

shape_base.py: Base Shape class

rectangles.py: Rectangle and Square

triangles.py: All triangle types

main.py: Test code for option 2

How to run


# Option 1 - Single module
bash

cd module_shapes
python main.py

# Option 2 - Separate modules
bash

cd individual_modules_shapes
python main.py