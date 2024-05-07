import random
import string

letter = string.ascii_letters #-->for random upercase and lowercase letters
# letter = string.ascii_lowercase #-->for lowercase letters
# letter = string.ascii_uppercase #-->for uppercase letters

random_letters = ''.join(random.sample(letter , 3)) #This will return 3 random letters as string
print(random_letters)