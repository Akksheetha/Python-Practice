class Area:
    def setDim(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def getArea(self):
        return self.length * self.breadth
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
rect = Area()
rect.setDim(l, b)
print("Area of rectangle:", rect.getArea())