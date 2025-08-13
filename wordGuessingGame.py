print("Guess a fast-food name within the 3 chances you have. Let's begin.")

import random #random module use to select anything randomly from given range

fastFoods = ['burger','pizza','pasta','hotdog','ramen','fries','sandwitch',
             'wages','bao']

fastFood = random.choice(fastFoods)

chances = 3 #chances user can have to guess correctly
while chances > 0:
    food = input("Guess a fast food item: ") #taking food name as user input from user 

    if food == fastFood:
        print("That is correct!")
        break
    elif food != fastFood:
        chances-=1
        print(f'Wrong guess mate! You have {chances} left.')
    elif chances == 0:
        print(f'You have {chances} left.')