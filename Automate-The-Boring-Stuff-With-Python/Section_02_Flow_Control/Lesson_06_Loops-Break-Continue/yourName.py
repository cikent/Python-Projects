# define a variable and set it to be an empty string
name = ''

# execute block when name doesn't equal 'your name'
while name != 'your name':
    # ask the user to input 'your name'
    print('Please type your name.')
    # update name variable to user's input
    name = input()

# exit While loop and print if user updated name's value correctly
print('Thank you!')
