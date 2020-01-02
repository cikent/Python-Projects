# import argv from system module
from sys import argv

# unpack argv into different variables
script, input_file = argv

# declare print_all method, which is designed to read whatever fileObject is specified
def print_all(f):
	print(">>> print_all: f=", f)
	print(f.read())
	print("<<< print_all: f=", f)

# seek to the 1st line of the fileObject
def rewind(f):
	print(">>> rewind: f=", f)
	f.seek(0)
	print("<<< rewind: f=", f)

# declare print_a_line method, pass it the line # to read and the fileObject
def print_a_line(line_count, f):
	print(">>> print_a_line: line_count=", line_count)
	print(line_count, f.readline())
	print("<<< print_a_line: line_count=", line_count)

# declare file variable and generate a fileObject from the inputted file
current_file = open(input_file)

# print to screen notification to user that the fileObject will be printed
print("First let's print the whole file:\n")

# print contents of fileObject to screen
print_all(current_file)

# print to screen notification to user that the fileObject will be reset to the start
print("Now let's rewind, kind of like a tape.")

# reset the fileObject state back to the 1st line
rewind(current_file)

# print to screen notification to user that 3 lines will be printed from the fileObject
print("Let's print three lines:")

# declare variable to represent the current line # that has focus & print that line # from the fileObject
current_line = 1
print_a_line(current_line, current_file) # current line is = 1
current_line += 1

# increment the line # then print the line from the fileObject
print_a_line(current_line, current_file) # current line is = 2
current_line += 1

# increment the line # then print the line from the fileObject
print_a_line(current_line, current_file) # current line is = 3

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


