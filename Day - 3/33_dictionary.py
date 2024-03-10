# Dictionaries are ordered collecton of data items. They store multiple items in a
#  single variable. Dictionary items are key-value pairs that are separated by commas
#  and enclodes within curly brackets{}

# dict = {'name' : "ANY" , 'class': 3 , 'value': True, 'marks': 19.5}

# print(dict['name'])
# print(dict['class'])
# print(dict['value'])
# print(dict['marks'])
# print(type(dict), dict)

# # print(dict['name2'])    #--> Both are same but if key is not found, this will show error
# print(dict.get('name2'))# whereas this will not show error and will show None.
# print(dict)
# print(dict.keys()) #--> To print all keys
# print(dict.values())#--> To print all values

# for key in dict.keys():
#     print(f'Value corresponding to key {key} is {dict[key]}')

# print(dict.items()) #--> To print all key-value pairs
# for key, value in dict.items():
#     print(f'Value corresponding to key {key} is {value}')


###                                       DICT METHODS:

  #  emp code : performence
dict1 = {122: 34 , 234 : 45 , 211 : 78 , 456 : 67}
dict2 = {345: 56, 783 : 98}

# dict1.update(dict2) #--> To update a dictionary
# dict1.clear() #--> To clear all elements to create a empty dictionary
# dict1.pop(122) #--> To remove a specific element 
# del dict1[122] #--> To delete specific element 
del dict1 #--> To delete a dictinary 
print(dict1)
