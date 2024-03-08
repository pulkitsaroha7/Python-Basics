# Recurrsion is the process of defining something in terms of itself

def factorial(n):
    if( n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(6))

# Quick quiz : Write a program to print the fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f0 + f1
# f(n) = f(n-1) + f(n-2)

def f(n):
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return f(n-1) + f(n-2)

print(f'{1}st value of fibonacci series is : {f(1)}')
print(f'{2}nd value of fibonacci series is : {f(2)}')
print(f'{3}rd value of fibonacci series is : {f(3)}')
print(f'{11}th value of fibonacci series is : {f(11)}')
print(f'{17}th value of fibonacci series is : {f(17)}')