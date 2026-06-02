class Circle:
    def __init__(self, radius=1.0, color="red"):
        self._radius = radius
        self._color = color
    def getRadius(self):
        return self._radius
    def getColor(self):
        return self._color
    def setRadius(self, radius):
        self._radius = radius
    def setColor(self, color):
        self._color = color
    def getArea(self):
        return 3.14159 * self._radius * self._radius
    def __str__(self):
        return f"Circle[radius={self._radius}, color={self._color}]"
c1 = Circle()
print(c1)
circle2=Circle(2.5)
print(circle2)
circle3=Circle(3.5,"blue")
print(circle3)