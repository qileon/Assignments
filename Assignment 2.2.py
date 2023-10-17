import random

number_to_guess = random.randint(0, 100)
attempts = 0

print("Welcome to the GUESS THE NUMBER!")
print("I'm thinking of a number between 0-100 and you have 5 attempts to guess. Good Luck!")

while attempts < 5:
    guess = int(input("Your guess?: "))

    if guess == number_to_guess:
        print("Congratulations! You guessed my number!")
        break
    elif guess < number_to_guess:
        print("Not bad. But I'm thinking higher.")
    else:
        print("Slow down. I'm thinking lower.")

    attempts += 1

if attempts == 5:
    print(f"Nice try but you've used all your guesses. I was thinking  {number_to_guess}.")