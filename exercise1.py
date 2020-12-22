# This program asks the user to guess a number giving them clues.

import random


def guessing_game():
    number = random.randint(0, 100)

    while True:
        answer = int(input("What's the number? "))
        if answer == number:
            print("That's right, you guessed it!")
            break
        elif answer > number:
            print("Too high!")
        else:
            print("Too low!")


guessing_game()
