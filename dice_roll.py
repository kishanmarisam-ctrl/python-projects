# die roll game #
import random

while True:
    choice = input("Do you want to roll the die? (y/n): ")
    if choice.lower() == 'y':
        print("Rolling the die...")
        print("You rolled a", random.randint(1, 6))
    elif choice.lower() == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
