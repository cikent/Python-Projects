while True:
    print('Who are you?')
    name = input()
    if name != 'Chris':
        continue
    print(f'Hello, {name}. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break

print('Access granted.')
