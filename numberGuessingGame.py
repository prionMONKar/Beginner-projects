print("Welcome to the game of Number Guessing. To do so you have only 5 chances. Let's begin.")

import random #random function uses to pick something randomly

low = int(input("Enter a number for lower bound: "))
high = int(input("Enter a number for higher bound: "))

print(f'you have to guess number from {low} to {high}')

n=5 #Here we set the number of chances user can have.
rand = random.randint(low, high)  #randint select a random integer using random function from given range

for i in range (n):
    numberFromUser = int(input("Guess a number: ")) #user have to input their guessed number
    if(numberFromUser < rand):
        print("Too Low")
        n=n-1  #Everytime user do a wrong guess one chance will be deducted from their total chances of guessing.
        print(f'You have {n} chances left.')
    elif(numberFromUser > rand):
        print("Too High")
        n=n-1
        print(f'You have {n} chances left.')
    elif(numberFromUser == rand):
        print("Correct")
        break #after successfully guessing the number, break statement will end the loop here by breking the loop.
    else:
        print(f'You have {n} chances left.')