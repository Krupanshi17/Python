"""
ABSTRACTION IN PYTHON

Abstraction hides internal implementation
and forces subclasses to implement required methods.

"""

from abc import ABC, abstractmethod

# 1. ABSTRACT BASE CLASS
"""
Shape is an abstract class.
It defines a common structure for all shapes.
"""

class Shape(ABC):

    @abstractmethod
    def area(self):
        """
        Abstract method.
        Every shape must define how area is calculated.
        """
        pass


# 2. CHILD CLASS IMPLEMENTATION

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# 3. USING ABSTRACTION

shapes = [
    Rectangle(10, 5),
    Circle(7)
]

for shape in shapes:
    print("Area:", shape.area())