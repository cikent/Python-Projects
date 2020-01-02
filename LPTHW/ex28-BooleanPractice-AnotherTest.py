#
# Boolean Practice
#
'''
1. True and True	; True
2. False and True	; False
3. 1 == 1 and 2 == 1	; False
4. "test" == "test"		; True
5. 1 == 1 or 2 != 1		; True
6. True and 1 == 1		; True
7. False and 0 != 0		; False
8. True or 1 == 1		; True
9. "test" == "testing"	; False
10. 1 != 0 and 2 == 1	; False
11. "test" != "testing"	; True
12. "test" == 1			; False
13. not (True and False)	; True
14. not (1 == 1 and 0 != 1)	; False
15. not (10 == 1 or 1000 == 1000)	; False
16. not (1 != 10 or 3 == 4)			; False
17. not ("testing" == "testing" and "Zed" == "Cool Guy")	; True
18. 1 == 1 and (not ("testing" == 1 or 1 == 0))				; True
19. "chunky" == "bacon" and (not (3 == 4 or 3 == 3))		; False
20. 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"));	False
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