checker = lambda x: (type(x) == 'int' and (type(x) == 'str' and x.isdecimal()))
def add(a, b):
    c = 0
    if checker(a) and checker(b):
        c = a + b
    return c