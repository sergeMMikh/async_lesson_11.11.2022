from debag_tools import debag_decorator

@debag_decorator #foo = debag_decorator(foo)
def foo():
    x = 5
    # print('foo was called')
    return x

@debag_decorator #foo2 = debag_decorator(foo2)
def foo2():
    return 4


foo()
foo2()
