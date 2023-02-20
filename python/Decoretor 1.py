def my_decorator(org_func):
    def wrapper_func(*args, **kwargs):
        print("Something is happening before the function is called.")
        return org_func(*args, **kwargs)

    return wrapper_func


@my_decorator 
def display():
    print("Hello!")


@my_decorator
def display_info(name, age):
    print('display_info ran wit arguments ({},{})'.format(name, age))


display_info('Misty', '25')
display( )