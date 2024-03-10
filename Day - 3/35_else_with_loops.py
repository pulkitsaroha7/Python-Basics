# Python allows us to use else keyword with for as well as while loops too. The else block appears after the body 
#  of the loop. The statements in the else block will be executed after all iterations are completed. The program 
#  exits the loop only after the else block is executed. IF we use break statement then else will not run as else
#  will only run after all iterations of the loop are completed.

for i in range(6):
    print(i)
else:
    print("NO value for i")

for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("NO value for i")