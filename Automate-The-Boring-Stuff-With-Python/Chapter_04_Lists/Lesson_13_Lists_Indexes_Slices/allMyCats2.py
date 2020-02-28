# Declare an empty List called catNames
catNames = []

while True:
    print(
        "Enter the name of cat "
        + str(len(catNames) + 1)
        + " (Or enter nothing to stop.):"
    )
    name = input()
    if name == "":
        break
    catNames = catNames + [name]  # list con'cat'entation :)

print("The cat names are:")
for name in catNames:
    print("    " + name)

