
class Animals():
    
    def animal_name(self):
        name = "animal name"
        self.name = name
    

class Pet(Animals):

    def pet_name(self):
        pet = "pet"
        self.pet = pet
       

class Dog(Pet):

    def bark(self):
        print(f"{self.name} the pet {self.pet} is barking...")


dhrumil = Dog()
dhrumil.name = "bruno"
dhrumil.pet = "tommy"
dhrumil.bark()

# Done with the multilevel inheritence