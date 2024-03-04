# 25) Quiz Game in Python


import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        play_game()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

def play_game():
    print("\nI have selected a random number between 1 and 100. Try to guess it!\n")

    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 2

    while attempts < max_attempts:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
