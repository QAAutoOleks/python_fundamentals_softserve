x = 100

def outer_func():
    x = 1000

    def inner_func():
        global x
        x = 10000
        print(f"Inner x = {x}")
    
    inner_func()
    print(f"Outer x = {x}\n")

    def inner_nonlocal():
        nonlocal x
        x = 999
        print(f"Inner_nonlocal x = {x}")
    
    inner_nonlocal()
    print(f"Updated outer x = {x}")

outer_func()
print(f"Global x = {x}")