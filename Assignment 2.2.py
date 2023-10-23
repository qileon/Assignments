import random

print("Welcome to the GUESS THE NUMBER!")
print("Choose a number between 0-100 and I will try to guess the number.")

low = 0
high = 100
attempts = 0

while attempts < 5:
    guess = random.randint(low, high)
    print("Is your number " + str(guess) + "?")
    response = input("Enter 'higher', 'lower', or 'yes': ").lower()

    if response == 'yes':
        print("Nailed it! Your number is " + str(guess) + ".")
        break
    elif response == 'higher':
        low = guess + 1
    elif response == 'lower':
        high = guess - 1
    else:
        print("Please enter 'higher', 'lower', or 'yes'.")

    attempts += 1

if attempts == 5:
    print("Oof, i lost... You win. Good Game!")

print("Thank you for playing!")
