# declare Integer Variables to hold values
people = 30
cars = 40
trucks = 15

# Logic Gate: is Car's more than People, if True, execute underlying block of code
if cars > people:
	print(f">>>>: cars = {cars}")
	print(f">>>>: people = {people}")
	print("We should take the cars.")

# Logic Gate: is People more than Cars, if True, execute underlying block of code
elif cars < people:
	print(f">>>>: cars = {cars}")
	print(f">>>>: people = {people}")
	print("We should not take the cars.")

# Logic Gate: If proceeding If's fail, execute underlying block of code
else:
	print("We can't decide.")

# Logic Gate: is Trucks's more than Cars, if True, execute underlying block of code
if trucks > cars:
	print("That's too many trucks.")

# Logic Gate: is Cars's more than Trucks, if True, execute underlying block of code
elif trucks < cars:
	print("Maybe we could take the trucks.")

# Logic Gate: If proceeding If's fail, execute underlying block of code
else:
	print("We still can't decide.")

# Logic Gate: is People more trhan Trucks, if True, execute underlying block of code
if people > trucks:
	print("Alright, let's just take the trucks.")

# Logic Gate: If proceeding If's fail, execute underlying block of code
else:
	print("Fine, let's stay home then.")


# increment the values of the variables
people += 5
cars -= 10
trucks *= 2

# Logic Gate: If, elif, else statement to determine whether or not all the vehicles have a driver
if people > cars + trucks:
	print("There are enough people for each vehicle to be driven!")

elif people < cars + trucks:
	print("There isn't enough people to drive all the vehicles.")

else:
	print("There is exactly one driver for each vehicle.")


'''
#######################################
Study Drill #1: 
- If the logic gate of the If statement is deemed to be True, then the underlying Code block is executed/run

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