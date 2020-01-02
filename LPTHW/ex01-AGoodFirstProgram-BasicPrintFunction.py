import datetime
import math
import os
import sys

Day = datetime.date.today()

print(sys.version)
print(sys.executable)

# print to screen using Print function; gotta start somewhere
print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print("Yay! Printing.")
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')
print(f"This is the current date: {Day}")
print("Yay! Printing.")
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

number = 0

while number < 10:
    print(f"Number is: {number} and less than 10.")
    number += 1

print(f"Number is now: {number}, which is ten!")
