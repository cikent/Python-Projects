# Extra Credit: Create another Error to indicate when the User has inputted a negative number
def validateUserInteger(userVar):
    try:
        if userVar is type(int):
            continue
    except ValueError:
        print('You did not enter a number.')
        try:
            if int(userVar) >= 0:
                continue
        except:
            print('You did not enter a positive number.')


print('How many cats do you have?')
numCats = input()
validateUserInteger(numCats)

if int(numCats) >= 4:
    print('That is a lot of cats.')
else:
    print('That is not that many cats.')
