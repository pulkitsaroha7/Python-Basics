name = input("Enter your name : ")
date = input("Enter the date : ")
letter = '''Dear {}
    You are selected!!
    {}'''
print(letter.format(name , date))