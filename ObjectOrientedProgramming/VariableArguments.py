class Circle:
    def __init__(self, *args):
        if len(args) == 0:
            self._radius = 1.0
            self._color = "red"
        elif len(args) == 1:
            self._radius = args[0]
            self._color = "red"
        elif len(args) == 2:
            self._radius = args[0]
            self._color = args[1]
        else:
            raise ValueError("Too many arguments")
    def getRadius(self):
        return self._radius
    def getColor(self):
        return self._color
    def __str__(self):
        return f"Circle[radius={self._radius}, color={self._color}]"
circle1 = Circle()
print(circle1)
circle2 = Circle(2.5)
print(circle2)
circle3 = Circle(3.5, "blue")
print(circle3)