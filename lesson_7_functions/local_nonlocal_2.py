x = 1
print("Local x_global = {}".format(id(x)))


def foo():
    x = 10
    print("Local x1 = {}".format(id(x)))

    def bar():
        global x
        x = 25
        print("Local x2 = {}".format(id(x)))

    print("Before calling bar:", x)
    bar()
    print("After calling bar:", x)

foo()
print("x in main:", x)
print("Local x_global = {}".format(id(x)))