x = 100
print(f"Id x1: {id(x)}")

def outer_func():
    x = 1000
    print(f"Id x2: {id(x)}")

    def inner_func():
        global x
        x = 10000
        print(f"Id x3: {id(x)}")
        print(f"Inner x = {x}")
    
    inner_func()
    print(f"Outer x = {x}\n")

    def inner_nonlocal():
        nonlocal x
        x = 999
        print(f"Id x4: {id(x)}")
        
        print(f"Inner_nonlocal x = {x}")
    
    inner_nonlocal()
    print(f"Updated outer x = {x}")

outer_func()
print(f"Global x = {x}")
print(f"Id x1: {id(x)}")