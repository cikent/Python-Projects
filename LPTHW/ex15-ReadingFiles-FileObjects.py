#importing argv module into the script
from sys import argv

# assigning the variables for argv
script, filename = argv

# creating a variable called Txt and assigning it to the contents of filename
txt = open(filename)

# print to screen the file name followed by the contents of the file
print(f"Your file [{filename}] is here:")
print(txt.read())

# print to screen further instructions
print("Type the filename again:")
# save the users input as a variable
fileAgain = input("> ")

# store the contents of the user specified file into a variable
txtAgain = open(fileAgain)

# print to screen the 2nd variable storing content
print(txtAgain.read())

# close both files that have been opened
close(txt)
close(txtAgain)



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
# 	3rd = Using repr to print out variables Example: print(">>>> argv=", repr(argv))
#	4th = Using Pydoc to read a command's description. Example: python -m pydoc <command>
#	5th = Trying to use Python via Powershell w/o 1st navigating to the Directory containing desired files
# }

# ++ Things to Remember ++
# =============================
# Escape Characters:
# -------------------------
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





