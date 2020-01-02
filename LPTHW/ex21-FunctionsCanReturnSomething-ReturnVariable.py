# define the function add
def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

# define the function subtract
def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

# define the function multiply
def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

# define the function divide
def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b

# print to screen a prompt about the following methods/functions being called
print("Let's do some math with just functions!")

# execute the functions
age = add(30, 5) # == 35
height = subtract(78, 4) # == 74
weight = multiply(90, 2) # == 180
iq = divide(100, 2) # == 50

# print to screen the values of each of the variables
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
# Puzzle #1
print("Here is the puzzle.")

puzzle1 = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", puzzle1, "Can you do it by hand?")

# Study Drill 3
print("Here is the puzzle.")

studyDrill3 = multiply(height, divide(weight, add(iq, subtract(age, 10))))
# puzzle2 == 177.6
print("That becomes: ", studyDrill3, "Can you do it by hand?")

# Study Drill 4
print("Here is the puzzle.")

studyDrill4 = divide(height, subtract(age, multiply(iq, add(weight, 10))))

print("That becomes: ", studyDrill4, "Can you do it by hand?")

# =======================================================================================
# ++ Study Drills ++
# =============================
# 1. Go back through and write a comment on what each line does.
# 2. Read each one backward or out loud to find your errors.
# 3. Annotate mistakes & avoid them in the future
# 4. Plus whatever the specific Lesson entails

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
# 
# When you run (”use” or ”call”) a function, check these things:
# 1. Did you call/use/run this function by typing its name?
# 2. Did you put the ( character after the name to run it?
# 3. Did you put the values you want into the parenthesis separated by commas?
# 4. Did you end the function call with a ) character?

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
# =============================