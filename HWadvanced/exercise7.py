import math

class Rectangle:
    name = "Rectangle"
    def __init__(self, width, height):
        if (type(width) is int or type(width) is float and\
            type(height) is int or type(height) is float)\
                and width >0 and height > 0:
            self.width = width
            self.height = height
        else:
            raise TypeError("The values must be positive numbers")

    def area(self):
        return self.height * self.width
r1 = Rectangle(4,8)
print(r1.area())