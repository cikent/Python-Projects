# Start of Practice Projects for Chapter 4
""" Requirements """
# Creat a function that takes a List as an Argument
# Return a String with all the Items in the List concatenated by: ', ' (Comma & a Space)
# Insert 'and' before the last Item is concatenated with the String
# Function should be able to work with any List value pass to it

# sample test list
spam = ['apples', 'bananas', 'tofu', 'cats']



def mergeList(anyList):
    # Declare an empty String    
    mergeWords = ''
    # For each word in the List, add it to mergeWords
    for item in anyList:
        # todo
        mergeWords += str(item + ', ')
        # mergeWords = mergeWords + str(anyList[len(anyList)])      # Comment out for debugging
    
    return mergeWords

print(spam)

newMessage = mergeList(spam)

print(newMessage)
