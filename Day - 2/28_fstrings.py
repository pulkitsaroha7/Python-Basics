# String formatting done earleir:
letter = "my name is {} and i am from {}"
name = "Hacker"
country = "India"
print(letter.format(name , country))
print(letter.format(country , name))

letter = "my name is {1} and i am from {0}"
print(letter.format(name , country))
print(letter.format(country , name))

print(f"We use fstring like this : I am {{name}} and I am from {{country}}")# --> To print {}
price = 49.089897
txt = f"For only {price:.2f} dollars"
print(txt)

# Now fstrings are used:

print(f"My name is {name} and i am from {country}")