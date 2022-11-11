import datetime
from functools import wraps


def debug_decorator(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        print(f'{old_function.__name__} was called')
        print(f'with{args} and {kwargs}')
        result = old_function(*args, **kwargs)
        print(f'{result} was returned')
        return result

    return new_function


def timer(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        start = datetime.datetime.now()
        print('________________')
        result = old_function(*args, **kwargs)
        end = datetime.datetime.now()
        work_time = end - start
        print(f'{old_function.__name__} was working {work_time}')
        print('________________')
        return result

    return new_function
