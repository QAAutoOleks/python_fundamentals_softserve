# a = 3
# b = a
# c = a
# print(id(b))
# print(id(c))

# a = "New name"
# print(id(b))

a = True
print(id(a))

b = False
print(id(b))

b = True
print(f"id(a) = {id(a)}", f"id(b) = {id(b)}")