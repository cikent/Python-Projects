# define spam
def spam(divideBy):
    while True:
        try:
            return 42 / divideBy
        except ZeroDivisionError:
            # updated the Exception to be in scope of a 'while clause' and ask user to provide new value before trying again
            divideBy = int(input("Error: Invalid argument. Please input another #: "))
            continue


print(spam(2))
print(spam(12))
print(spam(0))  # ERROR! -- this should cause and exception
print(spam(1))
print(spam(7))
