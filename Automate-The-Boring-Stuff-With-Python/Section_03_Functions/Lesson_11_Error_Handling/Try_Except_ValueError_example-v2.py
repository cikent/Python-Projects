# Extra Credit: Create another Error to indicate when the User has inputted a negative number

print('How many cats do you have?')
numCats = validateUserInteger()

try:
    if type(numCats) is int:
        try:
            if int(numCats) >= 0:
                if int(numCats) >= 4:
                    print('That is a lot of cats.')
                else:
                    print('That is not that many cats.')
        except:
            print('You did not enter a positive number.')
except ValueError:
    print('You did not enter a number.')
    

def validateUserInteger:
    while True:
        try:
            if numCats = type(int):
                True
            else:
                False
        except:
            print('Hello World')

