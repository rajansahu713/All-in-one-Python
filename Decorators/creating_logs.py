# Logging: Decorator to log function calls and their arguments.

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function
def my_function(x, y):
    return x + y

print(my_function(2, 3))