a = []
b = []
c = ()
d = ()

print(a is b) # False. List is mutable, so were created different objects
print(a == b) # True. Equal content

print(c is d) # True
print(c == d) # True
