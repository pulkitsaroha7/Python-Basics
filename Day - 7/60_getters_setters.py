# Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator

# It is important to note that the getters do not take any parameters and we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter

# getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden. This can be useful for encapsulation and data validation

class MyClass:
    def __init__(self , value):
        self._value = value
    
    def show(self):
        print(f"Value is {self._value}")

    @property # --> Getter
    def ten_value(self):
        return 10 * self._value
    
    @ten_value.setter# --> Setter 
    def ten_value(self , new_value):
        self._value = new_value
    

obj = MyClass(19)
print(obj.ten_value)
obj.show()
obj.ten_value = 20
print(obj.ten_value)
obj.show()
