# classes
class MyClass():
    my_name = 'Milo'

    def meow(self):
        print(f'{self.my_name} meows')

milo = MyClass()
milo.my_name
milo.meow()

class Pet():
    def __init__(self, pet_name, age=0):
        self.name = pet_name
        self.years_old = age

    def meow(self):
        print(f'{self.name} meows')

milo = Pet('Milo')
milo.name
milo.meow()

class Animal():
    num_instances = 0
    def __init__(self):
        Animal.num_instances += 1

    @classmethod
    def how_many_animals(cls):
        print(cls.num_instances)

milo = Animal()
emilio = Animal()
benji = Animal()
blue = Animal()
charlie = Animal()
Animal.how_many_animals()
print(Animal.num_instances)

# polymorphism
print(3)
print('5')

class Pet():
    def __init__(self, pet_name, owner_name):
        self.name = pet_name
        self.owner = owner_name

    def meow(self):
        print(f'{self.name} meows')
    
    def __str__(self) -> str:
        return f"{self.name}'s owner is {self.owner}"
    
    def __repr__(self) -> str:
        return f"Pet('{self.name}', '{self.owner}')"
    
my_pet = Pet('Milo', 'Ethan')
print(my_pet)
print(repr(my_pet))

# inheritance
class Vehicle():
    def __init__(self) -> None:
        self.num_wheels = 4

    def make_sound(self):
        print('vroom')

class Tricycle(Vehicle):
    def __init__(self) -> None:
        self.num_wheels = 3

super_sweet = Tricycle()
print(super_sweet.num_wheels)
super_sweet.make_sound()