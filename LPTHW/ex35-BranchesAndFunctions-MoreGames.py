# import the Module exit from the Sys Library
from sys import exit

# def the function gold room
def gold_room():
	# print to screen a question
	print("This room is full of gold. How much do you take?")

	# store the User's input to the question
	choice = input("> ")
	# evaluate the User's input and perform conditional actions based upon their response
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)
	else:
		dead("You greedy bastard!")

# def the function bear_room
def bear_room():
	# print to screen a series of prompts followed by a question
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	# store intial state of whether or not the Bear has moved from the default position
	bear_moved = False

	# cause this logic to continually execute while the Bear_room function / method is being run
	while True:
		# store the User's input to the question
		choice = input("> ")

		# evaluate the User's input and perform conditional actions based upon their response
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print("The bear has moved from the door.")
			print("You can go through it now.")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			dead("I got no idea what that means.")

# def the function cthulhu_room
def cthulhu_room():
	# print to screen a series of prompts followed by a question
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares as you and you go insane.")
	print("Do you flee for your life or eat your head?")

	# store the User's input to the question
	choice = input("> ")

	# evaluate the User's input and perform conditional actions based upon their response
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

# def the function dead
def dead(why):
	print(why, "Good job!")
	exit(0)

# def the function start
def start():
	# print to screen a series of prompts
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")

	# store the User's input to the question
	choice = input("> ")

	# evaluate the User's input and perform conditional actions based upon their response
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

# execute the method / function 'Start' to being the game
start()




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

# =============================
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
#	9th = Declared a variable to be assigned a User's input valut, but failed to write input before ("> ")
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
 
# When you run (”use” or ”call”) a function, check these things:
# 1. Did you call/use/run this function by typing its name?
# 2. Did you put the ( character after the name to run it?
# 3. Did you put the values you want into the parenthesis separated by commas?
# 4. Did you end the function call with a ) character?
# 
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