
##                               FOR LOOP
# name = "Abhishek"
# for i in name:
#     print(i)

# colours = ["Red" , "Green" , "Blue"]
# print(colours)
# for colour in colours:
#     print(colour)
#     for i in colour:
#         print(i)

# Syntax : range(start , stop , step value), step value is optional
# We can only give integers as step value argument. Giving floating point 
#  and 0 as arguement will give ERROR.
for i in range(5):   # 5 is exclusive, it is same as range(0 to n-1)
    print(i)

for i in range(1,5): # 1 is inclusive, it is same as range(1 to n-1)
    print(i)

for i in range(1 , 13 , 3): # 13 is exclusive
    print(i)

# for i in range(1 , 13 , 3.5): --> error 
#     print(i)

# for i in range(1 , 13 , 0): --> error
#     print(i)