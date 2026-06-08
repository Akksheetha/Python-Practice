class Circle:
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color
    def getRadius(self):
        return self.radius
    def getColor(self):
        return self.color
    def setRadius(self, radius):
        self.radius = radius
    def setColor(self, color):
        self.color = color
    def getArea(self):
        return 3.14159 * self.radius * self.radius
    def __str__(self):
        return f"Circle[radius={self.radius}, color={self.color}]"
c = Circle(2.5, "blue")
print(c)
print("Area:", c.getArea())