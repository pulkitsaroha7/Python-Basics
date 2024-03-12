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