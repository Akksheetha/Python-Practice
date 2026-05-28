class MyClass:
    x = 5
    def display(self):
        print("I am inside the function")
obj = MyClass()
print("State:",obj.x)
print("Behavior:")
obj.display()