# define a variable and set it to be an empty string
name = ''

# execute block when name doesn't equal 'your name'
while True:
    # ask the user to input 'your name'
    print('Please type your name.')
    # update name variable to user's input
    name = input()
    # break out of the loop once name equals 'your name'
    if name == 'your name':
        break

# print once user update the name value correctly
print('Thank you!')
