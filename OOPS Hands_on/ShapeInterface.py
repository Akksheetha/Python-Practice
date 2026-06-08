class IShape:
    def CalculateArea(self): pass
    def CalculatePerimeter(self): pass
class Rectangle(IShape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def CalculateArea(self):
        return self.w * self.h
    def CalculatePerimeter(self):
        return 2 * (self.w + self.h)
class Circle(IShape):
    def __init__(self, r):
        self.r = r
    def CalculateArea(self):
        return 3.14159 * self.r * self.r
    def CalculatePerimeter(self):
        return 2 * 3.14159 * self.r
rect = Rectangle(4, 5)
circ = Circle(3)
print("Rectangle Area:", rect.CalculateArea())
print("Circle Area:", circ.CalculateArea())