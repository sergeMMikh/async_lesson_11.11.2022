def debag_decorator(old_function):
    def new_function():
        print(f'{old_function.__name__} was called')
        result = old_function()
        print(f'{result} was returned')
        return result

    return new_function