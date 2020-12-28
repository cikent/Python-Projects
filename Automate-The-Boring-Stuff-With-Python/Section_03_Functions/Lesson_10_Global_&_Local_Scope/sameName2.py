# define spam
def spam():
    global eggs
    eggs = 'spam'


# define eggs at the Global scope
eggs = 'global'
spam()
print(eggs)
