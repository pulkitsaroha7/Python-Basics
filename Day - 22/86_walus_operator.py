# The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation. The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements

a = True
# print(a = None) #--> error
print(a := False)

n = [1 , 2 , 3 , 4 , 5]
while(a := len(n) > 0):
    print(n.pop())

# foods = list()
# while True:
#     food = input("Which food do you like? : ")
#     if food == 'quit'
#         break
#     foods.append(food)
# Instead of this :
foods = list()
while( food := input("which food do you like? : ") != 'quit'):
    foods.append(food)

