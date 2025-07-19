lst = input()
n = int(input())

list_of_int = [int(i.strip()) for i in lst.split(',')]
list_of_int.sort()

result = None
if n <= len(list_of_int):
    result = list_of_int[n-1]