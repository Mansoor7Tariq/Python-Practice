from abc import ABC, abstractmethod
# METHORD OVER RIDING

class Shapes(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shapes):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shapes):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


circle_obj = Circle(5)
rectangle_obj = Rectangle(4, 6)

print("Circle Area:", circle_obj.calculate_area())
print("Rectangle Area:", rectangle_obj.calculate_area())
