# import argv Module from sys
from sys import argv

# parse argv into 2 variables
script, user_name = argv
# declare variable prompt
# prompt = '> '
userInput = ">> "

# print to screen questions to the user and save the input from the 1st response
print(f"Hi, {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(userInput)

#print(f">>>> {userInput}")

# save the user's 2nd response
print(f"Where do you live {user_name}?")
lives = input(userInput)

# print(f">>>> {userInput}")

# save the user's 3rd response
print(f"What kind of computer do you have?")
computer = input(userInput)

# print(f">>>> {userInput}")

# print to screen a confirmation using the inputs from the user
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer}. Nice.
""")





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





