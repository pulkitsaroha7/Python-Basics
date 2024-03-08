# #                              DAY - 22 : Python Lists 
# 1) They are ordered collection of data items
# 2) They store multiple data items in a single variable
# 3) List items are separated by commas and enclosed by bracekets []
# 4) Lists are mutable(changable), we can change them after creation

# l = [ 3 , 4 , 5]
# print(l)
# print(l[0])
# print(l[1])
# print(l[2])
# l = [ 3 , 4 , 5 , "Ashish" , "Carry" , True , 34 , 434  , 343 , 56 , 31]
# print(l)
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[5])

# print(l[-2]) # --> Negative indexing. It is equal to len - index. Ex:
# print(l[len(l) - 2])
# print(l[6-2])
# print(l[4])

# print(l[:]) # --> This is equal to print(l[0:len(l)])
# print(l[2:])
# print(l[1:9])
# print(l[1:9:2]) # --> This is [start : end : jump]

# list comprehension : Creating list on the go
# lst = [i for i in range(4)]
# print(lst)
# lst =[i for i in range(10) if i%2==0]
# print(lst)
# lst = [i*i for i in range(10) if i%2==0]
# print(lst)
# sample = ["aman" , "atr" , "karan" , "rajat" , "sumit" , "ash"]
# names = [i for i in sample if len(i)>4]
# print(sample)
# print(names)

# #                              DAY - 23 : Lists methods
lst = [ 3, 4 , 64 , 56 , 34 , 2434, 67 , 56 , 32 , 67]
# lst.append(3)
lst.sort()
# lst.sort(reverse = True)
# lst.reverse()
# print(lst.index(56))
# print(lst.count(56))
# m = lst # --> This means m is refference to lst and changing m will also change lst
# m[0] = 0
# To copy a list into other list use this :
# m = lst.copy()
# m[0] = 0
# lst.insert(1 , 789)
# m = [789 , 910 , 1011]
# lst.extend(m) # --> This will update lst by concatinating it with m
# --> But if we want concatinate two list without update then we can do:
# k = m + lst
# print(k)
print(lst)