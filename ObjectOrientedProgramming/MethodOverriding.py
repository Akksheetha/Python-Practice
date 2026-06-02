class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def show(self):
        print('Details:', self.name, self.color, self.price)
    def max_speed(self):
        print('Vehicle max speed is 150')
    def change_gear(self):
        print('Vehicle change 6 gear')
class Car(Vehicle):
    def max_speed(self):
        super().max_speed()
        print('Car max speed is 240')
    def change_gear(self):
        print('Car change 7 gear')
car = Car('Car x1', 'Red', 20000)
car.show()
car.max_speed()
car.change_gear()
vehicle = Vehicle('Truck x1', 'White', 75000)
vehicle.show()
vehicle.max_speed()