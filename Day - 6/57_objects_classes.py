class Person():
    name = "Ramesh"
    occupation = "Engineer"
    networth = 10
    def info(self):
        print(f'{self.name} is a {self.occupation}')
    def val(self):
        return 3

a = Person()
b = Person()
c = Person()

b.name = "Suersh"
b.occupation = "HR"

c.name = "Nikk"
c.occupation = "Developer"

a.info()
b.info()
c.info()
print(a.val())