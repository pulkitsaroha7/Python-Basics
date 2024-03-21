# The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes. When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy
# class A:
#     def info(self):
#         print("This is parent class")
    
# class B(A):
#     def info(self):
#         super().info()
#         print("This is child class")
    
# b = B()
# b.info()

# We can also use super keword to call constructors

class A:
    def __init__(self , name , id):
        print("This is parent class")
        self.name = name
        self.id = id
    
class B(A):
    def __init__(self , name , id , lang):
        print("This is child class")
        super().__init__(name , id)
        self.lang = lang
    
a = B("Ashok" , 235 , "Python")
print(a.name)
print(a.id)
print(a.lang)
