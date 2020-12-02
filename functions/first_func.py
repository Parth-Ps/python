def outer_func():
    msg = 'Hii'

    def inner_func():
        print(msg)
    return inner_func()


outer_func()


# def square(x):
#     return x * x


# def cube(x):
#     return x * x * x


# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result


# squares = my_map(cube, [1, 2, 3, 4, 5])
# print(squares)

# def logger(msg):

#     def log_message():
#         print('Log:', msg)

#     return log_message


# log_hi = logger('Hello!!')
# log_hi()

# def html_tag(tag):

#     def wrap_text(msg):
#         print('<{0}>{1}<{0}>'.format(tag, msg))

#     return wrap_text


# print_h1 = html_tag('h1')
# print_h1('I am Free')
# print_h1('Repeat after Me')

# print_p = html_tag('Hello')
# print_p('Anonymous')
