import random


def generate_number():
    return random.randint(1, 100)


def guess_number(secret_number, guess):
    if guess < secret_number:
        return "Too low!"
    elif guess > secret_number:
        return "Too high!"
    else:
        return "Congratulations! You guessed it!"


def play_game():
    secret_number = generate_number()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    guesses = 0
    while True:
        guess = int(input("Your guess: "))
        guesses += 1

        result = guess_number(secret_number, guess)
        print(result)

        if guess == secret_number:
            print(f"You guessed the number in {guesses} guesses!")
            break


if __name__ == "__main__":
    play_game()