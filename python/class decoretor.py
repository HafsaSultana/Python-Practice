def my_decorator(org_func):
    def wrapper_func(*args, **kwargs):
        print("Something is happening before the function is called.")
        return org_func(*args, **kwargs)
    return wrapper_func


class decorator_class:
    def __init__(self, org_func):
        self.org_func = org_func

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.org_func.__name__))
        return self.org_func(*args, **kwargs)


@my_decorator
def display():
    print("Hello!")


@decorator_class
def display_info(name, age):
    print('display_info ran wit arguments ({},{})'.format(name, age))


display_info('Misty', '25')
display()
