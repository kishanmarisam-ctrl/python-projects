# Rock, Paper, Scissors Game #

import random

emojis = {"rock": "✊", "paper": "✋", "scissors": "✌️"}
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
while True:
    continue_game = input(
        ("Welcome to Rock, Paper, Scissors! Do you want to play? (y/n): ")
    ).lower()
    if continue_game == "y":
        computer_choice = random.choice(choices)
    elif continue_game == "n":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue
    user_choice = input("Enter rock, paper, or scissors (r,p,s): ").lower()
    if user_choice == "r" and computer_choice == "scissors" or user_choice == "p" and computer_choice == "rock" or user_choice == "s" and computer_choice == "paper":
        print(user_choice, emojis[computer_choice])
        print("Computer chose", computer_choice, emojis[computer_choice])
        print("Congratulations! You win!")
    elif user_choice == "r" and computer_choice == "paper" or user_choice == "p" and computer_choice == "scissors" or user_choice == "s" and computer_choice == "rock":
        print(user_choice, emojis[computer_choice])
        print("Computer chose", computer_choice, emojis[computer_choice])
        print("you lose! computer wins!")
    elif user_choice not in ("r", "p", "s"):
        print("Invalid input. Please enter rock, paper, or scissors (r,p,s).")
        break
    elif user_choice == computer_choice:
        print("It's a tie! Try again.")
