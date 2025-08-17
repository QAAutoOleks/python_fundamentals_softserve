def generetor_create(num):
    while num > 0:
        yield num
        num -= 1

value = generetor_create(5)
print(generetor_create(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value)) # StopIteration