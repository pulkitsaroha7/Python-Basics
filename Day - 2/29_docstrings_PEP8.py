# Docstrings are string literals that appear right after the definition of a function, class, method
#  or module. They are initialised just below function definition or just above function body

def square(a):
    '''This function takes an integer as input and returns square of that number as output. 
       This function is very efficient'''
    '''This function is very efficient'''# --> This will not be displayed
    return a*a
print(square.__doc__)
print(square(5))

# PEP8 is a document that provides guidelines and best practices on how to write python code
# The primary focus of PEP8 is to improve the readability and consistency of python code


# The zen of python --> It is an easter egg in python for python, it is a poem which somewhere
# defines the best practices for python programming. To see this poem use import this. 'this' is
# not used in any programmming practices, it is just used to see that easter egg or poem 
import this 