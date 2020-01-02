'''
# import argv from the sys module
from sys import argv
# import exists from the os.path module
from os.path import exists

# unpack argv into different variables
script, fromFile, toFile = argv

# print to screen a notification to the user what the script will do
print(f"Copying from {fromFile} to {toFile}")

# Open a file and store its contents in a fileObject
# inFile = open(fromFile)
# read the contents of the fileObject and save its value to a String
# inData = inFile.read()

## we could do these two on one line, how?
# 1st attempt to combine
# inData = inFile.read(open(fromFile))
# 2nd attempt to combine
# inFile = open(fromFile) inData = inFile.read()\
# 3rd attempt to combine
# inFile = open(fromFile), inData = inFile.read()
# 4th attempt to combine
inFile = open(fromFile); inData = inFile.read()

# print to screen the length of the string variable in bytes
print(f"The input file is {len(inData)} bytes long")

# print to screen whether or not the file to be created already exists or not
print(f"Does the output file exist? {exists(toFile)}")

# print to screen a prompt for the user to determine if they want to proceed or not
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# wait for User input, if not Control+C, script will progress
input()

# Open a file and store its contents in a 2nd fileObject (presently nothing)
outFile = open(toFile, 'w')
# Write the value of the String to the 2nd fileObject
outFile.write(inData)

# print to screen a prompt that the script is complete
print("Alright, all done.")

# close the open fileObjects
inFile.close()
outFile.close()
'''

##########################################
# 1st attempt to combine all relevant code into 1 line (Study Drill 1 & 2)
from sys import argv; from os.path import exists; script, fromFile, toFile = argv; inFile = open(fromFile); inData = inFile.read(); outFile = open(toFile, 'w'); outFile.write(inData); inFile.close(); outFile.close()


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
