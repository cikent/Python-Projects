# declare a String w/ 4 Format Command brackets inside
formatter = "{} {} {} {}"

# print formatter to screen with new Integers
print(formatter.format(1, 2, 3, 4))
# print formatter to screen with new Strings
print(formatter.format("one", "two", "three", "four"))
# print formatter to screen with new Boolean values
print(formatter.format(True, False, False, True))
# print formatter to screen using itself as the 4 argument's
print(formatter.format(formatter, formatter, formatter, formatter))

# print formatter to screen with new Strings, broken onto new lines
print(formatter.format(
	"I love you beyond", 
	"What words can express",
	"Actions can show",
	"Or time will tell",
))


# Study Drills
# 1. Go back through and write a comment on what each line does.
# 2. Read each one backward or out loud to find your errors.
# 3. Annotate mistakes & avoid them in the future

#List of Mistakes made while making Python Programs
# mistakes = {
	# 1st = Not remembering how to write an F-string
	# 2nd = Forgetting that Print Commands always end with the newline (\n) parameter unless otherwise specified
	# 3rd = 
# }