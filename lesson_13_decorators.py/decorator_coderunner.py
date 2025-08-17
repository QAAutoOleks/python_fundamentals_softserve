def add_tag(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return tag + func(*args, **kwargs)
        return wrapper
    return decorator


@add_tag("<strong>")
def get_message():
    return "Hello, World!"

print(get_message())