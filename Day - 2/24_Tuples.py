# #                              DAY - 24 : Python Tuples 
# 1) They are ordered collection of data items
# 2) They store multiple items in one single variable
# 3) Tuple items are separated by commas and enclosed within round brackets()
# 4) Tuples are immutable(unchangeable) as strings, we cant change them after creation.

tup = (1 , 2, 3 , "green" , True)
# print(type(tup) , tup)
# t = (1) # It is confusion for python that its int or tuple so it always shows int, to store it as
#         # tuple the syntax will be:
# r = (1,)
# print(type(t) , t)
# print(type(r) , r)
# tup[0] = 3 # --> This will throw an error as we cant change tuples


# Concept of negative indexing is same as lists in tuples 
# print(len(tup) , tup[-2])

# if 3 in tup:
#     print("Yes 3 is present in this tuple")

# We can do slicing in tuples but slicing will return a new tuple and will not change the orginal one
# tup2 = tup[2:4]
# tup3 = tup[:-2]
# tup4 = tup[:]
# print("tup 2 :", tup2)
# print("tup 3 :", tup3)
# print("tup 4 :", tup4)

# #                              DAY - 25 : Python Tuples Operations
# We cant directly do operations on tuples, we first need to convert them into list and then we can 
# apply operations on that list and then again we have to convert it into tuple

# countries = ("india" , "russia" , "germany")
# print("Countires are :", countries)
# temp = list(countries)
# temp.append("japan")
# temp.pop(2)
# temp[1] = "usa"
# countries = tuple(temp)
# print("Countires are :", countries)

        #  some tuple methods :

# continents = ("asia" , "europe" , "america" , "antartica" , "australia")
# earth = continents + countries
# print("Earth consists :", earth)

tup = (1, 2 , 34 , 2 , 2 , 1 , 3 , 34 , 32, 1 , 2 , 3)
print(tup.count(3))
print(tup.count(2))
print(tup.count(1))
print("\n")
print(tup.index(3))
print(tup.index(2))
print(tup.index(1))
print("\n")
print(tup.index(3 , -4 , -1)) # --> to see index in given range of index. index(num , start , end). start
                              #    is inclusive and end is exclusive
print(tup.index(3 , 8 , 11))
