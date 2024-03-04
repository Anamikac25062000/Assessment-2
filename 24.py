# 24) Implement the game rock, paper, scissors
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.


import random

def get_user_choice():
    """
    Function to get the user's choice (rock, paper, or scissors).
    """
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    """
    Function to get the computer's random choice (rock, paper, or scissors).
    """
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """
    Function to determine the winner of the game based on choices.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win! Congratulations!"
    else:
        return "You lose! Better luck next time."

# Main game loop
if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break
