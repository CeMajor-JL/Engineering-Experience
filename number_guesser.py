import random

def guess_the_number():
    print(" Welcome to Guess The Number")
    print("I'm thinking of a number between 1 and 100.")
    print("Type 'q' anytime to quit.\n")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Your guess: ")

        if guess.lower() == "q":
            print(" You quit. The number was:", secret)
            break

        if not guess.isdigit():
            print(" Enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print(" Too low.")
        elif guess > secret:
            print(" Too high.")
        else:
            print(f" Correct! You got it in {attempts} attempts.")
            break

def main():
    while True:
        guess_the_number()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print(" Game over. Brain gains secured.")
            break

main()