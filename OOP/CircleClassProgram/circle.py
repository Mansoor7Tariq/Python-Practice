import math


class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius


radius = float(input('Enter the radius of the circle: '))
circle_obj = Circle(radius)

print('The area is:', circle_obj.calculate_area())
print('The circumference is:', circle_obj.calculate_circumference())
