# Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class
class shape:
    def __init__(self , x , y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y
class circle(shape):
# Either we can do this:
    # def __init__(self , x):
    #     self.x = x
# or we can do this:
    def __init__(self , x):
        super().__init__(x , x)
    def area(self):
        return 3.14 * super().area()
    
c = circle(5)
print(c.area())
