# GUESS NUMBER GAME

import random
number = random.randint(1,100)
attempts = 0

print("please enter number between 1 and 100")
while True:
    guess = int(input('please enter a number'))
    attempts += 1

    if guess < number:
        print("too low")
    elif guess > number:
        print("too high")
    else:
        print(f"you correct guess number in {attempts} attempts")
        break


    