list1 = [1,2,3,4,5]

try:
    print(list1[5])
except Exception:
    print('Exception')
except IndexError:
    print('IndexError')

