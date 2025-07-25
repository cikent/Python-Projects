#! python 3

# Source PDF File location: https://2009-2017.state.gov/documents/organization/112065.pdf
# Create a Program to Search a PDF for all the viable Phone and Email values

# import relevant modules
import re, pyperclip

# TODO: Create a Regex for phone numbers
re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, x12345

((\d\d\d) | (\(\d\d\d\)))?            # area code (optional)
(\s|-)                                 # first seperator
\d\d\d                                 # first 3 digits
-                                      # seperator
\d\d\d\d                               # last 4 digits
(((ext(\.)?\s) |x)                      # extension word-part (optional)
 (\d{2,5}))?                           # extension number-part (optional)
''', re.VERBOSE)

# TODO: Create a Regex for email addressess

# TODO: Get the text off the clipboard

# TODO: Extract the email/phone from this text

# TODO: Copy the extracted email/phone to the clipboard