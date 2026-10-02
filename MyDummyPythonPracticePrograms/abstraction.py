#abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Create instances of Rectangle and Circle
rectangle = Rectangle(5, 3)
circle = Circle(4)

# Calculate and print areas
print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 15
print(f"Circle Area: {circle.area()}")        # Output: Circle Area: 50.24