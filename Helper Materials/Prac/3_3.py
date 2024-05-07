#Q) Write a program to detect double spaces in python
count = 0
str = input("Enter the string : ")
for i in range(len(str)-1):
    if str[i] == ' ':
        if str[i+1] == ' ':
            count+=1
print("Double space in your sting is :", count)