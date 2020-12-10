# greet User and ask for an input
print('Please input a value between 1 and 5 for Spam!')
# store user's input into the spam variable
spam = input()

# assess whether or not the user actually inputted in a value
if spam == '':
    print('You entered nothing... please input a value for Spam!')
# determine if spam == 1
elif spam == '1':
    print('Hello')
# determine if spam == 2
elif spam == '2':
    print('Howdy')
# determine if spam == anything else
else:
    print('Greetings!')
