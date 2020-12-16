"""
An elif (else if) statement can follow an if statement. Its block executes
if its condition is True and all of the previous conditions have been False.
"""
name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampir.')
elif age > 100:
    print('You are not Alice, grannie.')
    