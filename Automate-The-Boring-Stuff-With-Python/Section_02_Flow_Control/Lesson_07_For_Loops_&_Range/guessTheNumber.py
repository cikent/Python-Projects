""" This Program has the User guess a # between 1 and 20 and attempt to guess the correct answer within 6 attempts. """
import random

# intialize a variable to a random number between 1 and 20
secretNumber = random.randint(1, 20)
# print to screen a prompt
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    # store user's input in guess
    guess = int(input())

    # evaluate if guess is less or greater than secretNumber
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

# after the user has exhausted the # of guesss, evaluate the variable against the secretNumber
if guess == secretNumber:
    print('Good job! You guessed my number in ' +
          str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
