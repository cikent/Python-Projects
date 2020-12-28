# define spam
def spam():
    global eggs
    eggs = 'spam' # This variable has Global Scope

# define bacon
def bacon():
    eggs = 'bacon' # This variable has Local Scope
    
# define ham
def ham():
    print(eggs) # This variable has Global Scope

# declare the variable eggs
eggs = 42 # This variable has Global Scope

# call spam
spam()

# print value of eggs
print(eggs)
