# create a string variable and assign it a value
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# print to screen a prompt
print("Wait there are not 10 things in that list. Let's fix that.")

# create the List variable 'stuff' by parsing the string variable ten_things
stuff = ten_things.split(' ')
# create another list and fill it with string object variables
more_stuff = ["Day", "Night", "Song", "Frisbee",
			  "Corn", "Banana", "Girl", "Boy"]

# execute while stuff does not equal 10 entities
while len(stuff) != 10:
	next_one = more_stuff.pop() # 
	print("Adding: ", next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")

# print to screen a prompt and the variable stuff
print("There we go: ", stuff)

# print to scree a prompt
print("Let's do some things with stuff.")

# print to screen the 2nd index within the stuff list
print(stuff[1])
# print to screen the last index of the list
print(stuff[-1]) # whoa! fancy
# print to screen and remove the last index from the list
print(stuff.pop())
# print to screen stuff by removing the spaces with the join function
print(' '.join(stuff)) # what? cool!
# print to screen the 4th and 5th indices from the list with join using #
print('#'.join(stuff[3:5])) # super stellar!

'''
# debug print statement
print("There we go: ", stuff)

# example of executing another method against a list
stuff.remove('Oranges')

# debug print statement
print("There we go: ", stuff)
'''
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
#	9th = Declared a variable to be assigned a User's input valut, but failed to write input before ("> ")
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