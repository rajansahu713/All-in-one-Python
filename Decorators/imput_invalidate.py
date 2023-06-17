# Input Validation: Decorator to validate input arguments of a function.

def validate_input(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Input arguments must be integers")
        for value in kwargs.values():
            if not isinstance(value, int):
                raise TypeError("Keyword arguments must be integers")
        return func(*args, **kwargs)
    return wrapper

@validate_input
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))