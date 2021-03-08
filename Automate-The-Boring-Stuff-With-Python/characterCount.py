# Define a String
message = 'It was a bright cold day in April, and the clocks were stricking thirteen.'

# Define a empty Dictionary
count = {}

# Iterate through each character within the String 
for character in message:
    # Create a Key/value pair in the Count Dict for each unique Character value in message
    count.setdefault(character, 0)
    # Set the value of each Unique Key equal to the # of times that character is utilized within message
    count[character] = count[character] + 1

# Print to screen the value of Count
print(count)
