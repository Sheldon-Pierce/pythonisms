import time


def calculate_time(func):
    def wrapper(thing1, thing2):
        start_time = time.time()
        result = func(thing1, thing2)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time} seconds.")
        return result
    return wrapper


@calculate_time
def my_function(item):
    pass


my_function(item)

