import time
ques = ["Which two elements make up water?","What is the tallest mountain in Africa?","What is the name of the river that flows through Baghdad?",
           "Who painted the famous artwork 'The Starry Night'?", "Who wrote the novel 'One Hundred Years of Solitude'?", "What is the smallest country in the world by land area?",
           "Who wrote the novel '1984'?", "What is the name of the smallest bone in the human body?", "What is the name of the phenomenon that causes the sky to turn red during sunrise and sunset?",
           "Who composed the famous opera 'The Barber of Seville'?"]

ans = ["Carbon and Oxygen" , "Hydrogen and Nitrogen" , "Hydrogen and Oxygen" , "Helium and Oxygen" , "c" , "Mount Kilimanjaro" , "Mount Kenya" , "Mount Satima",
        "Mount Karisimbi" , "a" , "Nile" , "Euphrates" , "Amazon" , "Danube"  , "b" , "Vincent van Gogh" , "Pablo Picasso" , "Leonardo da Vinci" , "Claude Monet" , "a" ,  
        "William Shakespeare" , "Gabriel Garcia Marquez" , "Jane Austen" , "Charles Dickens"  , "b" , "San Marino" , "Monaco" , "Liechtenstein" , 
        "Vatican City" , "d" , "George Orwell" , "Aldous Huxley" , "Ray Bradbury" , "J.D. Salinger" , "a" , "Femur" , "Stapes" , "Tibia" , "Ulna" , "b" , "Rayleigh scattering",
        "Doppler effect" , "Reflection" , "Refraction" , "a" , "Giuseppe Verdi" , "Richard Wagner" , "Wolfgang Amadeus Mozart" , "Gioachino Rossini" , "d"]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
option = 0
j = 0
reward = 0
print("\n")
print("                          WELCOME TO KAUN BANEGA CROREPATI")
print("Rules:")
print("-There are total 10 questions, you will be given one chance to answer each question")
print("-If you give 3 correct answers, you will win Rs.3000")
print("-If you give 6 correct answers, you will win Rs.20000")
print("-If you give all correct answers, you will win Rs.320000")
print("-If you give any wrong answer then you will loose the game and will loose money")
print("-Quitting will make you win the last reward amount")
print("-You have no lifelines and you cannot use google to answer the questions")
print("\nGame starts :- ")
name = input("Enter your name : ")
print("\n")
for i in range(len(ques)):
    print(f'Your Question for Rs.{levels[i]} is:-\n{ques[i]}')
    print(f"options:    a) {ans[j]}    b) {ans[j+1]}    c) {ans[j+2]}    d) {ans[j+3]}    e) QUIT\n")
    option = input("Type your option : ")

    if(option == ans[j+4]):
        print(f"Your answer is correct , you have won Rs.{levels[i]}")
        if(i == 2):
            reward = 3000
        elif(i == 5):
            reward = 20000
        j += 5
    elif(option == 'e'):
        print(f"Dear {name} played very well, better luck next time, thankyou for playing\nThe amount you won : Rs.{reward}")
        break
    else:
        print("\n")
        reward = 0
        print("Your answer is wrong, you lost the game, AGLI BAAR THODA HOMEWORK AUR PADHAI KARKE AANA")
        print(f"Dear {name} better luck next time!")
        break   
    print("\n")
else:
    reward = 320000
    print(f"Congratulations {name}, You are the winner of Kaun Banega Crorepati")
    print(f'The amount you won : {reward}')
 