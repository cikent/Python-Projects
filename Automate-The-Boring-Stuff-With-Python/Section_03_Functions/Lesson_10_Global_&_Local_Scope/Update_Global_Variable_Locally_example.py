# Define spam: Calls a Global Variable and updates the value locally
def spam():
    global eggs
    eggs = 'Globally defined variable, updated in Local scope'      # This variable has Global Scope

# Define bacon
def bacon():
    eggs = 'Locally defined variable, but never called'             # This variable has Local Scope
    
# Define ham
def ham():
    print(eggs)                                                     # This variable has Global Scope

# Declare the variable eggs
eggs = 42                                                           # This variable has Global Scope

# Call spam and update the Global variable value for eggs
spam()

# Print value of eggs
print(eggs)
