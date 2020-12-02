# Decorators
# First class function allows us to treat any function like a object
# so example
# we can function as arugument to another function.
# we can return function or assign function to variables.

# Now, closures allow usto take advantages to first_class_function and return inner funcion that remember and access to variables local to the scopein which they were created.


# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     # If we remove parenthesis then it will wait for usto call. lets call it
#     return inner_function


# outer_function()
# here we call function.Remeber:- that clousure remeber our value so we can call many times and it still print the same resutl.
# hi_func = outer_function("HI")
# by_func = outer_function("by")

# hi_func()
# by_func()

# .................DECORATOR.............
# Decorator is the function that take another function as a arguments and add some kind of functionality and return without change to the actual function.


# def decorator_function(message):
#     def wrapper_function():
#         print(message)
#     return wrapper_function

# As we know decorator function as argument so lets change it to the decorator


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {} function".format(
            original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

# This is raw formation of decorato.It alternate is code is given below


# def display():
#     print("display function ran.")


# decorated_display = decorator_function(display)

# decorated_display()

# ............Typical decorator.....................


@decorator_function
def display():
    print("Display function ran..")


display()

# display = decorator_function(display)
# display()

# @decorator_function is equal to display = decorator_function(display) and then execute display()
# ..............end of decorator use.
# It basically use to add extra functionality without changing original functio.


# EXAMPLE: 2
# NOTE: if original function take arguments then we have to pass the *args and **kwargs to the original decorator function.
@decorator_function
def display_info(name, age):
    print("display_info ran with argument ( {}, {} )".format(name, age))


display_info("John", 25)

# .................USING DECORATOR CLASS TO DECORATE......


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("class method executed this before {} function".format(
            self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print("Display function ran..")


display()


@decorator_class
def display_info(name, age):
    print("display_info ran with argument ( {}, {} )".format(name, age))


display_info("John", 25)
