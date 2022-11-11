from debag_tools import debug_decorator, timer


@debug_decorator
@timer
def summator(a, b):
    return a + b


summator(3, 4)
