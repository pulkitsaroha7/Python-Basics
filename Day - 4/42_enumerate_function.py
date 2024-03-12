# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as list,
#  tuple or string) and get the index and value of each element at the same time.

fruits = ['mango' , 'orange' , 'apple' , 'banana']

# for index , fruit in enumerate(fruits):
#     print(index , fruit) #--> they will return as tuple

# index = 0
# for fruit in fruits:
#     print(fruit)                                  #--> This method not considered
#     if(index == 2):
#         print(f"{fruit} is Healthy and Tasty")
#     index += 1


for index , fruit in enumerate(fruits):
    print(fruit)
    if(index == 2):
        print(f"{fruit} is Healthy and Tasty")