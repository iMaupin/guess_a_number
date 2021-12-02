from art import logo
from random import randint
from os import system

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    chosen = False
    while not chosen:
        difficulty = input("Choose a difficulty 'easy' or 'hard':\n").lower()
        if difficulty == "easy" or difficulty == "hard":
            chosen = True
    attempts = EASY_LEVEL_TURNS if difficulty == "easy" else HARD_LEVEL_TURNS
    return attempts


def check_number(guess, answer, remaining_attempts):
    """Checks the answer and returns if it is guessed"""
    if remaining_attempts == 0:
        print("You have no remaining attmepts./nYou Lose.")
        return True
    elif guess == answer:
        print(f"You guessed {guess} and the answer is {answer}.\nYou Win!💥")
        return True
    elif guess > answer:
        print("Too high.\nGuess again.")
        return False
    elif guess < answer:
        print("Too low.\nGuess again.")
        return False


def run_game(attempts, answer):
    for attempt in range(attempts):
        remaining_attempts = attempts - attempt
        print(f"You have {remaining_attempts} remaining to guess the number.")
        guess = int(input("Make a guess:\n"))
        guessed = check_number(guess, answer, remaining_attempts)
        if guessed:
            break


def main():
    system("clear")
    print(logo)
    answer = randint(1, 100)
    print("Welcome to the number guessing game.\n I'm thinking of a number between 1 and 100.")
    attempts = set_difficulty()
    run_game(attempts, answer)


main()
