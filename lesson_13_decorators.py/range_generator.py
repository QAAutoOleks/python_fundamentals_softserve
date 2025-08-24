def range_generator(num):
    x = 0
    while x < num:
        yield x
        x += 1

# value = range_generator(5)
# print(value)
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))
