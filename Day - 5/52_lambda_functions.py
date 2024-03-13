# A lambda function is a small anynoymous functions without a name. 
# Lambda functons are often used in cases where a small one-line functon is required for short period of time.
# They are commonly used as arguments to other functons and higher order functons such as map, filter and reduce

def appl(fx , value): # passing function as argument
    return 6 + fx(value)

double = lambda x : x*2
cube = lambda x : x*x*x
avg = lambda x , y , z : (x + y + z)/3
print(double(5))
print(cube(5))
print(avg(4 , 4 , 4))
print(appl(lambda x : x*x , 2))