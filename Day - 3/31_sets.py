# Sets are unordered collection of data items. They store multiple data items in a single
#  variable. Items within sets are separated by commas and are enclosed in brackets{}. 
#  They are immutable(once created cannot be changed). The items in sets cannot be repeated
#  i.e, they dont contain duplicate values
# Order of items can change during every run so we can't access set items using indexing

# s = {2 , 3 , 4 , 2, 3}
# print(type(s) , s)

# set = {"Cars" , 4 , True , 12.3 , 4}
# print(set)


# Q) try to create an empty set and check its type.
#sol:

#pulkit = {} #--> This will not create an empty set as syntax of set and dict is same so it
            #   will always show type is dict, to create empty set do this:

#pulkit = set() #--> This is showing error in vscode but is running on other platforms
#print(type(pulkit))


# for accessing sets in Python we use for loop:
# for i in set:
#     print(i)



###                             Set Methods in Python

set1 = {1 , 2 , 4 , 5}
set2 = {2 , 4 , 6 , 7}

print(set1.union(set2))#-->This will not update the original one
# print(set1 , set2 )
set1.update(set2) #-->This will update the original one
print(set1 , set2 )
print(set1.intersection(set2))
print(set1 , set2 )
set1.intersection_update(set2)
print(set1 , set2 )
