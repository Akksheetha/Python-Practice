class Triangle:
    def __init__(self):
        self.a = 3
        self.b = 4
        self.c = 5
    def getPerimeter(self):
        return self.a + self.b + self.c
    def getArea(self):
        s = self.getPerimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
t = Triangle()
print("Perimeter:", t.getPerimeter())
print("Area:", t.getArea())