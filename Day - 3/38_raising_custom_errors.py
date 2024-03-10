# a = int(input("Enter any number between 5 and 9 : "))
# if (a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")

# Q) Raise a custom error whenever user enters a keyword other than 'quit'
# sol:
ip = input("Enter quit or else you will get an error : ")
if(ip != 'quit'):
    raise ValueError("Enter quit only")