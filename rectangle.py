""" rectangle """
class Rectangle:
    """ input """
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def calculate_area(self):
        """ input """
        area = self.height * self.width
        return area
    def calculate_perimeter(self):
        """ input """
        parameter = 2*(self.height+self.width)
        return parameter

rectangle = Rectangle(float(input()), float(input()))

condition = input()
if condition == "area":
    result = rectangle.calculate_area()
else:
    result = rectangle.calculate_perimeter()
print(f"{result:.2f}")
