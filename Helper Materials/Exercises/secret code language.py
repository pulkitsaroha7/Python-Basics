import random
import string
def encode(str):
    words = str.split(' ')
    words = list(words)
    i = 0
    for word in words:
        if(len(word)>= 3):
            letter = string.ascii_letters
            letter2 = string.ascii_letters
            random_letters = ''.join(random.sample(letter , 3))
            random_letters2 = ''.join(random.sample(letter2 , 3))
            # words[i] = f'{random_letters}{word[1:]}{word[0]}{random_letters2}'   
            words[i] = random_letters + word[1:] + word[0] + random_letters2
        elif(len(word)== 2):
            # temp = word[0]
            # temp2 = word[1]
            # words[i] = f'{temp2}{temp}' # To reverse a string instead of these 3 lines use this line:
            words[i] = word[::-1] # reversing a string
        i += 1
    words = tuple(words)       
    print("Encoded text is :", ' '.join(words)) # To join string either do this or use these lines:
    # print("Encided text is : ", end=' ')
    # for word in words:
    #     print(f'{word}', end=' ')
    return words
    
def decode(words):
    words = list(words)
    i = 0
    for word in words:
        if(len(word) == 2):
            # temp = word[0]
            # temp2 = word[1]
            # words[i] = f'{temp2}{temp}'
            words[i] = word[::-1]
        elif(len(word) > 2):
            index = len(word) - 4
            words[i] = word[index] + word[3:index] # Use this or this:
            # first_word = main_word[len(main_word)-1]
            # index = len(main_word)-1
            # words[i] = f'{first_word}{main_word[:index]}'
        i += 1
    words = tuple(words)
    print("Decoded text is :", ' '.join(words))
    # print("Decoded text is :", end = ' ')
    # for word in words:
    #     print(f'{word}', end = ' ')

ans = 'n'
while(ans != 'y'):
    str = input("\nEnter your message : ")
    ans2 = input("\nYou want to encode('y' to encode and 'n' to exit) : ")
    if(ans2 == 'y'):
        str = encode(str)
        ans2 = input("\n\nDo you want to decode it('y' to decode and 'n' to exit) : ")
        if(ans2 == 'y'):
            decode(str)
            print('\n')
        else:
            ans = input("\nDo you want to exit the program('y' to exit and 'n' to continue) : ")
        ans = input("\nDo you want to exit the program('y' to exit and 'n' to continue) : ")
    else:
        ans = input("\nDo you want to exit the program('y' to exit and 'n' to continue) : ")



