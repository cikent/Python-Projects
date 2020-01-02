# define the function cheese_and_crackers, it requires 2 arguments when run/use/called
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
# 	print(f"You have {cheese_count} cheeses!")
# 	print(f"You have {boxes_of_crackers} boxes of crackers!")
# 	print("Man that's enough for a party!")
# 	print("Get a blanket. \n")

# run cheese_and_crackers using integers as arguments
# print("We can just give the function numbers directly:")
# cheese_and_crackers(20, 30)

# run cheese_and_crackers using variables as agruments
# print("OR, we can use variables from our scripts:")
# amount_of_cheese = 10
# amount_of_crackers = 50

# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# run cheese_and_crackers using integers + math as arguments
# print("We can even do math inside too:")
# cheese_and_crackers(10 + 20, 5 + 6)

# run cheese_and_crackers using variables + integers + math as arguments
# print("And we can combine that two, variables and math:")
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# =======================================================================================
# Exercise 19 Study Drill # 3
# =======================================================================================
from datetime import date

currentDate = str(date.today())
currentYear = int(currentDate[:4])
currentMonth = int(currentDate[5:7])
currentDay = int(currentDate[-2:])

print(">>>> currentDate: ", repr(currentDate))
print(">>>> currentYear: ", repr(currentYear))
print(">>>> currentMonth: ", repr(currentMonth))
print(">>>> currentDay: ", repr(currentDay))

def name_and_age(userName, userBirthday):
	# parse the User's age
	userBirthYear = int(userBirthday[-4:])
	userBirthMonth = int(userBirthday[:2])
	userBirthDay = int(userBirthday[2:4])

	print(">>>> userBirthYear: ", repr(userBirthYear))
	print(">>>> userBirthMonth: ", repr(userBirthMonth))
	print(">>>> userBirthDay: ", repr(userBirthDay))

	# calculate the # of years since birth
	if (currentMonth >= userBirthMonth) & (currentDay >= userBirthDay):
		userYearAge = abs(currentYear-userBirthYear)
	else:
		userYearAge = abs((currentYear-userBirthYear)-1)
	
	# calculate the # of months since birth
	if (currentMonth >= userBirthMonth) & (currentDay >= userBirthDay):
		userMonthAge = abs(currentMonth-userBirthMonth)
	else:
		userMonthAge = abs(abs(currentMonth-userBirthMonth)-12)
	
	# calculate the # of days since birth
	if currentDay >= userBirthDay:
			userDayAge = abs(currentDay-userBirthDay)
	else:
		if currentMonth == (1 or 3 or 5 or 7 or 8 or 10 or 12):
			userDayAge = abs(abs(currentDay-userBirthDay)-31)
		elif currentMonth == (4 or 6 or 9 or 1):
			userDayAge = abs(abs(currentDay-userBirthDay)-30)
		else:
			userDayAge = abs(abs(currentDay-userBirthday)-28)

	# print to screen the user's name and age
	print(f"So your name is {userName} and you are currently {userYearAge} years, {userMonthAge} months and {userDayAge} days old!?")


userName = str(input("What is your name?: "))
userBirthday = str(input("What year were you born?\nPlease enter it in the following format \"MMDDYYYY\": "))


# name_and_birthday(userName, userBirthyear)
name_and_age(userName, userBirthday)


'''
Known Defects:
1) If User B-day is greater than present day but in the same Month; month is calculated wrong
2) 

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


