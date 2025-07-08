print(45<32 or [] or None or [10])
# output is [10], not True

print(100 < 50 or not [10] and True and "True" or 0)
#         1         4         2        3         5
# ultimately output is 0