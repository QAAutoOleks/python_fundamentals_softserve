def stars(some_func):
    def inner(*args, **kwargs):
        print('*' * 30)
        some_func(*args, **kwargs)
        print('*' * 30)

    return inner

def percents(some_func):
    def inner(*args, **kwargs):
        print('%' * 30)
        some_func(*args, **kwargs)
        print('%' * 30)

    return inner

@percents
@stars
def printer(text):
    print(text)

printer('Hi!')