# ^ means the string must start with pattern, $ means the string must end with the pattern. Both means the entire string must match the entire pattern.
# The . dot is a wildcard; it matches any character except newlines.
# Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
# Pass re.I as the second argument to re.compile() to make the matching case-insensitive.

# import the Regex modole
import re

# Create a String Variable to contain sample text
roboPrimeDir = 'Serve the public Trust. \nProtect the Innocent. \nUphold the Law.'

# Create a Dot Star Sign Character Class to find anything that matches the pattern BUT does NOT return New Line Values
datStarNoNewLineRegex = re.compile(r'.*')

# Create a Dot Star Sign Character Class to find anything that matches the pattern using the DOTALL argument
datStarNewLineRegex = re.compile(r'.*', re.DOTALL)

# Utilize re.search() to return a List of all the matches and create a variable to store the data
dotStarNoNewLineReturnValue = datStarNoNewLineRegex.search(roboPrimeDir)
dotStarNewLineReturnValue = datStarNewLineRegex.search(roboPrimeDir)

# Print to screen the output of the Regex expressions
print(dotStarNoNewLineReturnValue)
print(dotStarNewLineReturnValue)
