"""
=== NUMBER GUESSING GAME ===
I'm thinking of a number between 1-100
You have 7 attempts

Attempt 1/7
Your guess: 50
Too high!

Attempt 2/7
Your guess: 25
Too low!

Attempt 3/7
Your guess: 37
Too high!

Attempt 4/7
Your guess: 31
Too low!

Attempt 5/7
Your guess: 34
🎉 Correct! You won in 5 attempts!

Play again? (yes/no): no
Thanks for playing!
"""

import random
actual= random.randint(1,100)


def checker(actual):
    x = 1
    while True:
        if x == 8:
            print("You are out of attempt buddy!")
            print(f"Game over! The number was {actual}")  
            break
        else:
            print(f"Attempt {x}/7")
            guess = int(input("Your guess: "))
            if guess == actual:
               print(f"Correct! You won in {x} attempts!")
               break
            elif guess < actual :
               print("Too low!")  
            elif guess > actual :
               print("Too high!")  
             
            x += 1


print("""
=== NUMBER GUESSING GAME ===
I'm thinking of a number between 1-100
You have 7 attempts""")
checker(actual)
while True:
    repete = input("Play again? (yes/no):").lower()
    if repete == 'no':
        print("Thanks for playing!")
        exit()
    elif repete == 'yes':
        actual= random.randint(1,100)
        checker(actual)
        

