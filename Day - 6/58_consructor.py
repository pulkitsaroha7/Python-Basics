class Person:
    # def __init__(self): # DEFAULT CONSTRUCTOR
    #     print("Hey I am a person, give me name and occupation")

    def __init__(self, name , occ): # PARAMERTERISED CONSTRUCTOR
        self.name = name
        self.occ = occ
        
    def info(self):
        print(f'{self.name} is a {self.occ}')
    

# a = Person()
b = Person("Aman", "CA")
b.info()
