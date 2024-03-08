# ##                                                DAY - 20
# def avr(a , b):
#     print("Average is :",(a*b)/(a+b))

# def sum(a , b):
#     print("Sum is :",(a+b))

# def dif(a , b):
#     print("difference is : ", a/b)

# def div(a , b):
#     print("Division is :", a/b)

# def operations(a , b):
#     avr(a,b)
#     sum(a,b)
#     dif(a,b)
#     div(a,b)
# choice = "YES"
# while(choice == "YES"):
#     print("\n")
#     a = int(input("Enter the first number : "))
#     b = int(input("Enter the second number : "))
#     operations(a,b)
#     choice = input("Enter YES to repeat program and NO for stoping program : ")
# print("Program ended")




##                                                DAY - 21
'''  We can have Four types of function arguments :
  i) Required arguments
 ii) Default arguments
iii) keyword arguments
 iv) Variable length arguments      '''
# def average(a , b): # --> required arguments
#     print("Average is :", (a + b)/2)

# def average(a = 9 , b = 1):# --> Default arguments
#     print("Average is :", (a + b)/2)
# average(3)
# average(b = 3)

# def three(a=3 , b=4 , c=5): # --> Keyword argument where every argument is identified by a key by interpreter i.e, key = value
#                             #     this give us leisure to change order of arguments. here keys are a , b , c
#     print("Average is :", (a + b + c)/3)
# three(b=4,a=14,c=4)

def average(*number):# Variable arguments : where we can pass as many as arguments as we can bcoz they are stored as tuples
    print(type(number))
    sum = 0
    for i in number:
        sum = sum + i
    #print("Average is :", sum/len(number))
    return sum/len(number)

average(5 , 8 , 34 , 56, 1 , 45 , 2)

def name(**name):# --> arguments will be passed as dictionary
    print(type(name))
    print("Your name is :", name["name"], name["mname"], name["lname"])

name(name = "Yamla" , mname = "Pagla" , lname = "Deewana")
c = average(3 , 4 , 5)
print(c)