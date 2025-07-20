lst = input()
num = int(input())

int_list = [int(i.strip()) for i in lst.split(',')]
int_list.sort()

counter = 0
for element in int_list:
    if element < num:
        counter += 1
    else:
        result = round(100 * (len(int_list) - counter) / \
                       len(int_list), 1)

print(result)