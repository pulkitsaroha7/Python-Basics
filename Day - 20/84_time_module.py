import time
# def usingFor():
#     for i in range(10000):
#         print(i)

# def usingWhile():
#     i = 0
#     while i<10000:
#         print(i)
#         i = i + 1

# init = time.time() #--> It will count time in seconds from 1 Jan 1960
# usingFor()
# t1 = time.time() - init
# init = time.time() 
# usingWhile()
# print(time.time() - init)
# print(t1)



# for i in range(5):
#     print(i)
#     time.sleep(2) # it pauses time for n seconds


t = time.localtime() #--> It will return local time but in a very unreadable format
# print(t , type(t))
formatted_time = time.strftime("%y-%m-%d %H-%M-%S" , t)
print(formatted_time , type(formatted_time)) # It will return time in readable and str format

