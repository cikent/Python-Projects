# define the Collatz Sequence
def collatz(collatzNumber):
    # todo while collatzNumber > 1:
    if collatzNumber % 2 == 0:
        print(collatzNumber // 2)
        return collatzNumber
    else:
        print((3 * collatzNumber) + 1)
        return (3 * collatzNumber) + 1


# Ask User to define a #
def askUserForNumber():
    while True:
        try:
            # continue to ask this question until User provides a valid #
            userNumber = int(input("Please input any number: "))
            return userNumber
        except ValueError:
            # prompt User they inputted a non-valid value, ask them to try again
            print("That was not a valid Number, please try again.")


# run askUserForNumber
collatzNumber = askUserForNumber()

# todo (fix the looping issue)
while collatzNumber > 1:
    collatz(collatzNumber)
