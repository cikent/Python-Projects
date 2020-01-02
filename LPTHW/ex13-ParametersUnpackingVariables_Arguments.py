# modify script to require arguments when used
from sys import argv

# parse the arguments provided into distinct variables
script, first, second, third = argv

print(">>>> argv=", repr(argv))

# print the 1st argument associated with when the script is run
print("The script is called:", script)
# print the 2nd argument associated with when the script is run
print("Your first variable is:", first)
# print the 3rd argument associated with when the script is run
print("Your second variable is:", second)
# print the 4th argument associated with when the script is run
print("Your third variable is:", third)

# ask the user what they want to do now
userInput = input("\nWhat do you want to do now? ")

# print to screen the value the user provided
print(f"\nSo, you're interested in {userInput} next?! Cool!")

# ask the user their Age
userAge = int(input("\nHow old are you? "))

# print to screen the value the user provided
print(f"\nand you're {userAge} years old?")

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





