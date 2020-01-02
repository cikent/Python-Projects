"""
Python Command and Character list From Learn Python the Hardway by Zed Shaw (expanded from Lesson 22)    			
"""				

### Character / Command    What it's called    What it does    example    example2     ###
pydoc <something>	#pydoc	gives you the manual page for something you want to know about in python	pydoc sys	
help()	#help function	use when running python to find help on an object		
print()	#print function	prints to the console whatever is next	print(“Hello World!”)	print(1 + 2)
" "	# double quotes	starts and ends a string	print(“Hello World!”)	
' '	# single quotes	starts and ends a string	print('Hello World!')	
=	# equals	assigns values to a variable or function	count = 10	i, j, k, numbers = initialize()
#	pound	comment; blocks out the line from being read by the interpreter	# This is a comment and won't do anything	
;	# semi-colon	let's you separate multiple lines of code on one line	from sys import argv; from os.path import exists; script, from_file, to_file = argv	
:	# colon	used for defining things like in functions; tells python you are going to create a new "block" of code" followed by a new line with 4 indented spaces and then code.	def some_function():	
,	# comma	separates strings from variables	print "The script is called:", script	
+	# plus	adds	2+2 equals 4	
-	# minus	subtracts	etc.	
/	# slash	divides, allows you to continue a line of code on multiple lines	etc.	
*	# asterik	multiplies, wild card	from ex25 import *	
%	# 1. percent	gives the remainder of a divisor	7 % 6 returns 1	
%	# 2. String Fornatter	converts something to something in a string	http://docs.python.org/2/library/stdtypes.html#string-formatting-operations	
%d, %r, %s	# escape characters	let's you insert the contents of a variable into a string. %d is for display, %r is for debugging, %s is for inserting / converting to a string. there are others as well...	print "You have this many %d potatoes." % potatoes	
( )	# paranthesis	for multiple escape character variables, functions	print("Some string {0} {1}".format(variable1, variable2))	some_function()
<	# greater than	comparison operator	if buses > cars: print "Too many buses."	
>	# less than	comparison operator		
<=	# greater than or equal to	comparison operator		
>=	# less than or equal to	comparison operator		
==	# is equal to	comparison operator		
!=	# does not equal	comparison operator		
_	# underscore charcter	generally used instead of spaces	number_passengers	
\	# backslash	let's you "escape" certain characters in python	print "I have a \"stupid\" cat." print "I am 5'8\" tall."	
\n	# newline character (backslash n)	inserts a new line		
\t	# tab	inserts a tab	print(""" I'll do a list: \n\t*beer \n\t*chips \n\t*salsa """)	
""" """	# triple double quotes	lets you type a comment on mulitple lines, as long as you have """ at the begining and end	"""This is some code that does blah blah blah"""	
raw_input() # raw input (built in function)	takes input in the form a string from the user	you can prompt the user by doing: raw_input("user give me some data")	var = raw_input("> ")
input()	# input function (built in)	takes input in the form of a integer from the user	age = input("What's your age? ")	
import	# import statement	adds native python modules	from sys import argv	
sys	# sys module	provides access to some objects used or maintained by the interpreter and to functions that interact strongly with the interpreter	from sys import argv	
argv	# argument variable	see pydoc sys	script, filename = argv	
os.path	# path module			
exists	# exists command	returns true / false if a file exists or not		
int()	# convert to integer function	takes a number and makes it an integer	int(3.33) would return 3	
float()	# convert to a floating point number	"" makes it a float	float(3) would return 3.0	
open()	# open function	built in function for opening files	text = open(some_file)	
read()	# read function	reads the contents of the script. see pydoc file	print(text.read())	
close()	# close function	closes the file	text.close()	
write(stuff) # write function	writes stuff to the file	text.write(stuff)	
truncate() # truncate function	empties the file	text.truncate()	
seek()	# seek	takes you to specific line in a file	def rewind(f): f.seek(0)	
range()	# range	adds a range of integers to a list. range(1,6) will return 0, 1, 2, 3, 4, 5. You can also specify the step in the 3rd number eg: range(1,6,2) will return 0, 2, 4	<<<	
append() # append	appends object(s) to the end of the list		
.	# period/dot	lets you call functions on variables or string connect multiple functions	open(to_file, 'w').write(indata) OR output.close()	
def	# define	defines a function in a script		
return	# return	returns something to the console from within a funciton		
[ ]	# brackets	for containing lists	fruit = ['apples', 'oranges', bananas'] coins = [1, 5, 10, 25]
