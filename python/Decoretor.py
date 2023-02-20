def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
print('----------###############------------\n')


def smart_div(func):
    def inner(a, b):
        # print('hi', a, b)
        if a < b:
            a, b = b, a
        print('In inner', func(a, b))

    return inner


@smart_div
def div(a, b):
    print('In div', (a / b))

    return 'hello'


# def div(a, b, c=None):
#     if c is None:
#         print(a / b)
#     else:
#         print(a / b + c)


# div1 = smart_div(div)  #inner
# div1(3,6) # inner

div(3, 6)
