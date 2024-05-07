import random

def check(user , CPU):
    if(user == CPU):
        return 0
    
    if(user == 0 and CPU == 2):
        return -1
    
    if(user == 1 and CPU == 0):
        return -1
    
    if(user == 2 and CPU == 1):
        return -1
    
    return 1
def score(result):
    global cpup
    global userp
    if(result == 0):
        print(" DRAW ")
        print(f'Your score : {userp}      CPU score : {cpup}')
    if(result == -1):
        print(" YOU WIN ")
        userp += 1
        print(f'Your score : {userp}      CPU score : {cpup}')
    if(result == 1):
        print(" CPU WINS ")
        cpup += 1
        print(f'Your score : {userp}      CPU score : {cpup}')
    
cpup = 0
userp = 0
while(1>0):
    CPU = random.randint(0 , 2)
    user = int(input("\nEnter your choice [ snake(0) water(1) gun(2) quit(-1) ] : "))
    if(user == -1):
        if(userp > cpup):
            print("You are the winner\n")
            break
        else:
            print("CPU is the winner, Get some luck and retry after some time\n")
            break
    else:
        score(check(user , CPU))
    