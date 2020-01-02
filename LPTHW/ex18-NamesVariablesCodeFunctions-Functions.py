# this one is like your scripts with argv
# define the function print_two
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
# define the function print_two_again
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
# define the function print_one
def print_one(arg1):
	print(f"arg1: {arg1}")

# this one takes no arguments
# define the function print_none
def print_none():
	print("I got nothin'.")

# execute each of the newly created functions by passing in the correct # of arguments
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

'''
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
# }


# ++ Things to Remember ++
# =============================
Function Checklist:
# =============================
1. Did you start your function definition with def?
2. Does your function name have only characters and _ (underscore) characters?
3. Did you put an open parenthesis ( right after the function name?
4. Did you put your arguments after the parenthesis ( separated by commas?
5. Did you make each argument unique (meaning no duplicated names)?
6. Did you put a close parenthesis and a colon ): after the arguments?
7. Did you indent all lines of code you want in the function four spaces? No more, no less.
8. Did you ”end” your function by going back to writing with no indent (dedenting we call it)?

When you run (”use” or ”call”) a function, check these things:
1. Did you call/use/run this function by typing its name?
2. Did you put the ( character after the name to run it?
3. Did you put the values you want into the parenthesis separated by commas?
4. Did you end the function call with a ) character?

Use these two checklists on the remaining lessons until you do not need them anymore.
Finally, repeat this a few times to yourself:
	”To ’ run , ’ ’ c a l l , ’ or ’ use ’ a function a l l mean the same thing . ”
'''

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


