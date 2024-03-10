def func():
    try:
        lst = [1 , 23, 44]
        i = int(input("Enter the index : "))
        print(lst[i])
        return 1
    except:
        print("Some error occcured")
        return 0
    #print("End of try-except block and i am always executed")

# This print will not get printed but if we want to execute lines of code we can use finally
# Either try or catch block executes, it will always run even after returning values. 
# **imp** Mostly it is used to execute lines of code in a function even after returning values
    
    finally:
        print("End of try-except block and i am always executed")

x = func()
print(x)