x = 100

def outer_func():
    x = 1000

    def inner_func():
        global x
        x = 10000
        print(f"Inner x = {x}")
    
    inner_func()
    print(f"Outer x = {x}")

outer_func()
print(f"Global x = {x}")