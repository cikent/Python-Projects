"""This program says hello and asks for the users name and age"""

# display initial greeting
print('Hello World!')

# ask the user for their name
print('What is your name?')

# store the user's input as their Name value
userName = input()

# greet user by their name and print the length of their name
print('It is good to meet you, ' + userName)
print('Your name is ' + str(len(userName)) + ' characters long!')

print('What is your age?')          # ask for their age
# store the user's input as the Age value
userAge = input()
# print User's Age 1 year from now
print('You will be ' + str(int(userAge) + 1) + ' in a year.')
