# Extra Credit: Create another Error to indicate when the User has inputted a negative number
def validateUserInteger():
    global numCats

    try:
        if numCats = int(numCats):
            continue
    except ValueError:
        print('You did not enter a number.')
        validateUserInteger()
        try:
            if int(numCats) >= 0:
                continue
        except:
                print('You did not enter a positive number.')
                validateUserInteger()


print('How many cats do you have?')
numCats = input()
validateUserInteger()

if int(numCats) >= 4:
    print('That is a lot of cats.')
else:
    print('That is not that many cats.')
