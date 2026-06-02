from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woo!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
def print_animal_sound(animal:Animal):
        print(animal.make_sound())
dog = Dog()
cat = Cat()
print_animal_sound(dog)
print_animal_sound(cat)

