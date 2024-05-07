#Q) Write a program to detect double spaces and replace them with single spaces in python 
count = 0
str = input("Enter the string : ")
for i in range(len(str)-1):
    if str[i] == ' ':
        if str[i+1] == ' ':
            count+=1
print("Double space in initial string is :", count)
str2 = str.replace('  ' , ' ')
print("Your final string is : ", str2)
