lst = input()
list_int_not_increased = [int(i.strip()) for i in lst.split(',')]

result = []
for j, a in enumerate(list_int_not_increased):
    result.append(j + a)

print(result)