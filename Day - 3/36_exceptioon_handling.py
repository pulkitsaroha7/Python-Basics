a = input("Enter the value of a : ")
print(f"Multiplication table of {a} is :")
try:
    for i in range(1,11):
        print(f'{int(a)} x {i} = {int(a) * i}')
except:
    print("Invalid Input")

print("End of try-except block")

try:
    num = int(input("Enter an integer : "))
    a = [5 , 6]
    print(a[num])
except ValueError:
    print("The number is not an integer")
except IndexError:
    print("Index error")    

print("End of try-except block")