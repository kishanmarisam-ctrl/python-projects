import random

number_to_guess = random.randint(1, 100)
attempts = 10

while attempts > 0:
    prompt = ("Welcome to the Number Guessing Game! "
              "I'm thinking of a number between 1 and 100. "
              "You have 10 attempts to guess it. Enter your guess: ")
    guess = int(input(prompt))
    attempts -= 1

    if number_to_guess == guess:
        print("Congratulations! You've guessed the number correctly!")
        break
    elif number_to_guess > guess:
        print("Too low! Try again.")
    elif number_to_guess < guess:
        print("Too high! Try again.")

if attempts == 0:
    print("Game over! You've used all your attempts. The number was",
          number_to_guess, ". Better luck next time!")

elif not isinstance(guess, int):
    print("Invalid input. Please enter a number between 1 and 100.")
