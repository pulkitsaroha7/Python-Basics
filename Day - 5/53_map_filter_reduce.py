# In python map, filter and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequnence. These funcitons are known as higher order functions, as they take other functions as thier arguments 
# MAP: The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. 
# FILTER: The filter function filters a sequence of elements based on a given predicate(a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate


# def cube(x):
#     return x*x*x

l = [1 , 2 , 4 , 5 , 3 , 2 , 6]
# newl = []
# for item in l:
#     newl.append(cube(item))

# newl = list(map(cube,l))# map return map object so we need to type caste it in a list,  tuple etc
newl = list(map(lambda x : x*x*x , l))
print(newl)

newnewl = list(filter(lambda x : x>4 , l))
print(newnewl)

from  functools import reduce # we can't use reduce without importing it
sum = reduce(lambda x,y : x+y , l)
# l = [1 , 2 , 4 , 5 , 3 , 2 , 6]
#     [3 , 4 , 5 , 3 , 2 , 6]
#     [7 , 5 , 3 , 2 , 6]
#     [12 , 3 , 2 , 6]
#     [15 , 2 , 6]
#     [17 , 6]
#     [23]
print(sum)