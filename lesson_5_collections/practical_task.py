lst = input()
list_int_not_increased = [int(i.strip()) for i in lst.split(',')]

result = []
a = 0
for j in list_int_not_increased:
    result.append(j + a)
    a += 1