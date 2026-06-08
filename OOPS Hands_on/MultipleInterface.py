class Vehicle:
    def start(self): pass
    def stop(self): pass
class ElectricVehicle:
    def charge(self): pass
class GasVehicle:
    def refuel(self): pass
class ElectricCar(Vehicle, ElectricVehicle):
    def start(self): print("Electric car starting silently.")
    def stop(self): print("Electric car stopping.")
    def charge(self): print("Electric car plugging into charger.")
class GasMotorcycle(Vehicle, GasVehicle):
    def start(self): print("Motorcycle engine roaring to life.")
    def stop(self): print("Motorcycle turning off.")
    def refuel(self): print("Filling gas tank.")
car = ElectricCar()
bike = GasMotorcycle()
car.start()
car.charge()
bike.start()
bike.refuel()