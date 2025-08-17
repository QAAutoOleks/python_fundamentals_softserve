def fibonacci_numbers():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_numbers()
for i in range(10):
    print(next(fib))


# from functools import reduce

# def fibonacci_numbers(num):
#     iter = 0
#     x1 = 0
#     x2 = 0
#     while iter < num:
#         if x2 >= 2:
#             yield x2
#             x1, x2 = x2, x1
#             x2 += x1
#         elif x1 == 1 and x2 == 1:
#             yield x2
#             x2 += x1
#         elif x1 == 1 and not x2:
#             yield 1
#             x2 += x1
#         elif x1 == 0:
#             yield 0
#             x1 += 1
#         iter += 1

    
# fib = fibonacci_numbers(10)
# print(fib)
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))