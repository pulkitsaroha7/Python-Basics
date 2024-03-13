x = 10  #global variable(A variable defined outside the function and can be accessed anywhere
#        in the program and in a function too as long as any local variable of same name is
#         not present)


print("Global variable before chnage :" , x)
def change():
    global x  # global key word is used to use global variable in function and changes done in
            #   function will affect the original also
    x = 5
    y = 3 # local variable
    print("Local variable y is" , y)

change()
print("Global variable after chnage :" , x)