n = int(input())
n_string = str(n)

sum = 0
quantity_of_iteration = 0
for i in n_string:
    sum += int(i)
    quantity_of_iteration += 1

float_result = round(sum / quantity_of_iteration, 0)
result = int(float_result)
print(result)