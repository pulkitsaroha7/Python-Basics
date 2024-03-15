# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often reffered to as a decorated function.

# def greet(fx):# --> Decorator function
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx

def greet(fx):# --> Decorator function for a function which contains arguments
    def mfx(*arg , **kwarg):
        print("Good Morning")
        fx(*arg , **kwarg)
        print("Thanks for using this function")
    return mfx


@greet
def hello():
    print("Hello world")

@greet
def add(x , y , z):
    print(x+y+z) 

# greet(hello)()# --> Either use this line or @greet
hello()
add(1 , 2 , 3)

