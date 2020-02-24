# define the Collatz Sequence
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number
    else:
        print((3 * number) + 1)
        return (3 * number) + 1


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


# todo
collatz(askUserForNumber())

