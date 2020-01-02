# declare 3 lists and assign values to the entities
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Study Drill #3 example
fruits_length = len(fruits)
copy_fruits = fruits.copy()

# Study Drill #3 example
print(f"This is the # of entities in 'copy_fruits': {copy_fruits}")

# Study Drill #3 example
copy_fruits.clear()

# Study Drill #3 example
print(f"This is the # of entities in 'copy_fruits': {copy_fruits}")

# this first kind of for-loop goes through a list
for number in the_count:
	print(f"This is count {number}")

# same as above
for fruit in fruits:
	print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
for i in change:
	print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print(f"Adding {i} to the list.")
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print(f"Elements was: {i}")


# =============================
# Things to Research:
# =============================
# Errors
# Hexidecimal
# Port
# TCP
# UDP
# Hypertext

# =============================
# ++ Study Drills ++
# =============================
# 1. Go back through and write a comment on what each line does.
# 2. Read each one backward or out loud to find your errors.
# 3. Annotate mistakes & avoid them in the future
# 4. Plus whatever the specific Lesson entails

# =============================
#  Pydoc Module Commands:
# =============================
# -k <keyword> | Argument: Search for a <keyword>
# -n <keyword> | Argument: Start an HTTP server with the given hostname <keyword>
# -p <keyword> | Argument: Start an HTTP server with the given port on the local machine. <keyword>

# =============================
# Mistakes
# =============================
# mistakes = {
# 	1st = Not remembering how to write an F-string
# 	2nd = Forgetting that Print Commands always end with the newline (\n) parameter unless otherwise specified
# 	3rd = Using repr to print out variables Example: print(">>>> object=", repr(object))
#	4th = Using Pydoc to read a command's description. Example: python -m pydoc <command>
#	5th = Trying to use Python via Powershell w/o 1st navigating to the Directory containing desired files
#	6th = Trying to print a fileObject before closing it
#	7th = Declaring Variables explicitly by Type
#	8th = False and False == False, not True
# }
 
# ++ Things to Remember ++
# =============================
# Function Checklist:
# =============================
# 1. Did you start your function definition with def?
# 2. Does your function name have only characters and _ (underscore) characters?
# 3. Did you put an open parenthesis ( right after the function name?
# 4. Did you put your parameters after the parenthesis ( separated by commas?
# 5. Did you make each parameter unique (meaning no duplicated names)?
# 6. Did you put a close parenthesis and a colon ): after the parameters?
# 7. Did you indent all lines of code you want in the function four spaces? No more, no less.
# 8. Did you ”end” your function by going back to writing with no indent (dedenting we call it)?
 
# When you run (”use” or ”call”) a function, check these things:
# 1. Did you call/use/run this function by typing its name?
# 2. Did you put the ( character after the name to run it?
# 3. Did you put the values you want into the parenthesis separated by commas?
# 4. Did you end the function call with a ) character?
# 
# Use these two checklists on the remaining lessons until you do not need them anymore.
# Finally, repeat this a few times to yourself:
# 	”To ’run', ’call' or ’use’ a function all mean the same thing.”

# =============================
#  Escape Characters:
# =============================
# Command | What id Does
# \\ | Backslash (\)
# \' | Single-quote (')
# \" | Double-quote (")
# \a | ASCII bell (BEL)
# \b | ASCII backspace (BS)
# \f | ASCII formfeed (FF)
# \n | ASCII linefeed (LF)
# \N{name} | Character named name in the Unicode database (Unicode only)
# \r | Carriage Return (CR)
# \t | Horizontal Tab
# \uxxxx | Character with 16-bit hex value xxxx
# \Uxxxxxxxx | Character with 16-bit hex value xxxxxxxx
# \v | ASCII vertical tab (VT)
# \ooo | Character with octal value ooo
# \xhh | Character with hex value hh