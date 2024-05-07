# import time
# print(time.strftime('%H:%M:%S'))
# if(time.strftime('%H')>= '6'and time.strftime('%H') < '12'):
#     print("Good Morning")
# elif(time.strftime('%H')>= '12' and time.strftime('%H') < '15'):
#     print("Good Afternoon")
# else:
#     print("Good Night")
import time
print(time.strftime('%H:%M:%S'))
if(int(time.strftime('%H'))>= 6 and int(time.strftime('%H')) < 12):
    print("Good Morning")
elif(int(time.strftime('%H'))>= 12 and int(time.strftime('%H')) < 15):
    print("Good Afternoon")
else:
    print("Good Night")