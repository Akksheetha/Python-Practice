class Circle:

    def __init__(self, radius=1.0, color="red"):
        self._radius = radius
        self._color = color


    @classmethod
    def withRadius(cls, radius):
        return cls(radius)


    @classmethod
    def withRadiusAndColor(cls, radius, color):
        return cls(radius, color)


    def getRadius(self):
        return self._radius


    def getColor(self):
        return self._color


    def __str__(self):
        return f"Circle[radius={self._radius}, color={self._color}]"


c1 = Circle()
print(c1)

circle2 = Circle(2.5)
print(circle2)

circle3 = Circle(3.5, "blue")
print(circle3)