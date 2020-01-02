# declare 3 Integer variables and assign their values
people = 20
cats = 30
dogs = 15


# If statement to determine if people are less than Cats
if people < cats:
	print("Too many cats! The world is doomed!")

# If statement to determine if people are more than Cats
if people > cats:
	print("Not many cats! The world is saved!")

# If statement to determine if people are less than Dogs
if people < dogs:
	print("The world is drooled on!")

# If statement to determine if people are more than Dogs
if people > dogs:
	print("The world is dry!")

# Increment the Dogs variable by 5
dogs += 5

# If statement to determine if people are greater than or equal to Dogs
if people >= dogs:
	print("People are greater than or equal to dogs.")

# If statement to determine if people are less than or equal to Dogs
if people <= dogs:
	print("People are less than or equal to dogs.")

# If statement to determine if people are equal to Dogs
if people == dogs:
	print("People are dogs.")

'''
#######################################
Study Drill #1: 
- If the logic gate of the If statement is deemed to be True, then the underlying Code is executed/run

Study Drill #2: 
- To help distinguish that it is contingent on the If-Statement; much
like the section of Code associated with a Function/method defintion

Study Drill #3: 
- That section of Code won't be related to the If-statement logic, it will be read independently from it

Study Drill #4: 
- Yes, because the If-statement and the parameters provide, if valid, can be evaluated against 
one another such that a Value of True or False can be derived

Study Drill #5: 
- Would depend on the values the parameters contain.
#######################################
'''

# =============================
# Things to Research:
# =============================
# Errors
# Hexidecimal
# 
# =============================
# ++ Study Drills ++
# =============================
# 1. Go back through and write a comment on what each line does.
# 2. Read each one backward or out loud to find your errors.
# 3. Annotate mistakes & avoid them in the future
# 4. Plus whatever the specific Lesson entails
# 
# 
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
# 
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
# 
# When you run (”use” or ”call”) a function, check these things:
# 1. Did you call/use/run this function by typing its name?
# 2. Did you put the ( character after the name to run it?
# 3. Did you put the values you want into the parenthesis separated by commas?
# 4. Did you end the function call with a ) character?
# 
# Use these two checklists on the remaining lessons until you do not need them anymore.
# Finally, repeat this a few times to yourself:
# 	”To ’run', ’call' or ’use’ a function all mean the same thing.”
# 
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