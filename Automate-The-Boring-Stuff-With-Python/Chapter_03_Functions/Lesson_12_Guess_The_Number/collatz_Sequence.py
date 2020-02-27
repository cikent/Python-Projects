# define the Collatz Sequence
def collatz(number):
    if number % 2 == 0:             # if # is even
        print(number // 2)          # print 
        return number // 2
    else:
        print((3 * number) + 1)
        return (3 * number) + 1


# Ask User to define a #
def askUserForNumber():
    while True:
        try:
            # continue to ask this question until User provides a valid #
            userNumber = int(input("Please input any whole number: "))
            # return userNumber
            return userNumber
        except ValueError:
            # prompt User they inputted a non-valid value, ask them to try again
            print("That was not a whole number, please try again.")


# declare a variable and set it to the value of askUserForNumber()
collatzNumber = askUserForNumber()

# execute while Collatz Number != 1
while collatzNumber != 1:
    collatzNumber = collatz(collatzNumber)

