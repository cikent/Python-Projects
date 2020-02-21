# define spam
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))      # ERROR! -- this should cause and exception
print(spam(1))
print(spam(7))
