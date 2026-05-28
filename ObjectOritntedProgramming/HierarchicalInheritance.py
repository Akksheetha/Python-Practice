class num:
    def __init__(self):
        self.x = 20
        self.y = 10

class add(num):
    def findSum(self):
        self.z = self.x + self.y
        print("Sum is :",self.z)
class sub(num):
    def findSub(self):
        self.z = self.x - self.y
        print("Sub is :",self.z)

obj1 = add()
obj1.findSum()
obj2 = sub()
obj2.findSub()
