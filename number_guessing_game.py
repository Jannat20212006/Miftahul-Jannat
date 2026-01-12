"""
Number Guessing Game
--------------------
The computer picks a number between 1 and 100.
The player must guess it, and gets hints (Too High / Too Low).
The game shows how many attempts were taken.
The game keeps running until the player chooses to exit.
"""

import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("I have chosen a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        guess = input("Enter your guess: ")
        
        # simple validation (still required for basic correctness)
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too Low!")
        elif guess > number:
            print("Too High!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.\n")
            break


def main():
    print("=== NUMBER GUESSING GAME ===")
    
    while True:
        play_game()
        again = input("Play again? (yes/no): ").strip().lower()
        
        if again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()