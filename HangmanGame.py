# Hangman game is a game where a random secret word will be guessed from secret word list
# user have to guess character by character, if one character matches then the chaaracter will be visible. By guessing each character perfectly the secret will be revealed otherwise you will be failed.

import random
from collections import Counter

fastFoods = '''burger pizza pasta hotdog ramen fries sandwitch wages bao'''

fastFoods = fastFoods.split(' ') #here we have splitted the words with spaces in between 

word = random.choice(fastFoods) #choose the word randomly

if __name__ == '__main__':
    print("Guess a word! Hint: the word will be fast food.")
    
    for i in (word):
        print('_', end=' ') #printed _ as same as the length of the random word
    print()

    playing = True

    letterGuessed = '' #n empty string to store the guessed character input from user
    chances = len(word)+2  #user can have the chances two more than the word length choosed randomly
    correct = 0
    flag = 0 #flag value will be changed after succesfully guessed the word
    
    try:
        while(chances!=0) and flag==0: #as long as the chances are remaining and the flg value is zero the game will  be continue unless the user interrupt
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter.')
                continue

            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess)>1:
                print('Enter only a single LETTER')
                continue
            elif guess in letterGuessed:
                print('You have already guessed the letter')
                continue

            if guess in word:
                k=word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
                    
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed)) != Counter(word):
                    print(char, end=' ')
                    correct += 1

                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print("Congratulations, You won!")
                    break  #break out of for loop
                    break  #break out of while loop
                else:
                    print('_',end=' ')

        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print("You lost! Try again...")
            print(f'The word was {word}')
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()