##
class Pet():
    num_instances = 0
    def __init__(self, pet_name):
        self.name = pet_name
        Pet.num_instances +=1

    def meow(self):
        print(f'{self.name} meows')
        
    @classmethod
    def how_many_animals(cls):
        print(cls.num_instances)


milo = Pet('milo')
milo.name
milo.meow()
Pet.how_many_animals()