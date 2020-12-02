def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):

    if y == 0:
        raise ValueError('can not be divided by Zero')
    return x / y
