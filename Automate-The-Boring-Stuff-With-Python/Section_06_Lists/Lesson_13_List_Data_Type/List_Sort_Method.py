# Declare a List value
diablo3Classes = ['Witch Doctor', 'Demon Hunter', 'Monk', 'Wizard', 'Necromancer', 'Crusader', 'Barbarian']
print('Print the initial list: \n' + str(diablo3Classes))

# Sort the List
diablo3Classes.sort()
print('The sort() method returns the list in ascending order: \n' + str(diablo3Classes))

# Reverse Sort the List
diablo3Classes.sort(reverse=True)
print('The sort(reverse=True) method returns the list in descending order: \n' + str(diablo3Classes))

# Declare a new List value
diablo3_diablo2Classes = ['paladin', 'sorceress', 'amazon', 'necromancer', 'assassin', 'barbarian', 'druid', 'Witch Doctor', 'Demon Hunter', 'Monk', 'Wizard', 'Necromancer', 'Crusader', 'Barbarian']
print('Print the new list: \n' + str(diablo3_diablo2Classes))

# Sort the List in actual alphabetical order
diablo3_diablo2Classes.sort(key=str.lower)
print('The sort(key=str.lower) method returns the list in alphabetical order: \n' + str(diablo3_diablo2Classes))