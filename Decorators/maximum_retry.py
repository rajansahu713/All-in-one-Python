# Retry on Exception: Decorator to retry a function a specified number of times upon exception.
import time
def retry_on_exception(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Exception occurred: {e}")
                    attempts += 1
                    time.sleep(1)
            print(f"Max attempts reached. Function failed.")
        return wrapper
    return decorator

@retry_on_exception(max_attempts=3)
def my_function():
    if random.random() < 0.5:
        raise ValueError("Random error occurred")
    else:
        return "Success"

my_function()