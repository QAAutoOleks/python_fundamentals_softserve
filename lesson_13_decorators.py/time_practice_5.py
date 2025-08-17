from functools import reduce


given_list = [4, -5, 0, 100, 3.45]

def define_max(a, b):
    return a if a > b else b

result_1 = reduce(lambda a, b: a if a > b else b, given_list)
result_2 = reduce(define_max, given_list)

print(result_1) # int
print(result_2) # int