# import library and module dependencies
import random

# declare an Integer and set it to a random value between 1 and 20
secretNumber = random.randint(1, 20)

# prompt the User
print("I am thinking of a number between 1 and 20. Can you guess what it is?")

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break  # This condition is the correct guess!

# output results from the User's guesses
if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
