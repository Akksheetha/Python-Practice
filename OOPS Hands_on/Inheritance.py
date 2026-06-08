class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def displayInfo(self):
        print(f"Brand: {self.brand}, Year: {self.year}")
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    def displayCarInfo(self):
        print(f"Brand: {self.brand}, Year: {self.year}, Model: {self.model}")
my_car = Car("Toyota", 2022, "Camry")
my_car.displayCarInfo()