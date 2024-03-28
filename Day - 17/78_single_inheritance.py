# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat
class animal:
    def __init__(self , name , species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Sound made by Animal is stored here")

    def pet(self):
        print("Animal can be kept as pet or not is mentioned here")
    
    def diet(self):
        print("Food items commonly eaten by Animal is mentioned here")

class cat(animal):
    def __init__(self , name):
        self.name = name
    
    def make_sound(self):
        print("Meow")
    def pet(self):
        print("Can be kept as pet")
    def diet(self):
        print("Milk")
    
a = animal("tiger" , "bengal")
a.make_sound()
a.pet()
a.diet()

cat = cat("billu")
cat.make_sound()
cat.pet()
cat.diet()
