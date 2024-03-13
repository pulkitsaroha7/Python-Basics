# In python, is and == are comparison operators that can be used to check if two values are equal or not. However, there are some differences between them

# for immutable objects python allocate same memory space for eg
a = 3
b = 3 
tupa = (1 , 2 , 3) 
tupb = (1 , 2 , 3)
# constant 3 and (1 , 2 , 3) are stored at same memory location but with 2 diff variables i.e, a , b and tupa and tupb
lsta = [2 , 3 , 4]
lstb = [2 , 3 , 4]
# lists are immutable hence they both are stored at diff locations
print(a is b) # is compare exact location of objects in memory
print(a == b) # == compares values
print('\n')
print(tupa is tupb)
print(tupa == tupb)
print('\n')
print(lsta is lstb)
print(lsta == lstb)
