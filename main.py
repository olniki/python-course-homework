import inspect


# Write a decorator that ensures a function is only called by users with a specific role.
# Each function should have an user_type with a string type in kwargs
def is_admin(func):
    def wrapper(*args, **kwargs):
        if kwargs['user_type'] == 'admin':
            func(*args, **kwargs)
        else:
            print('Permission denied')

    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    print('Successfully executed')


show_customer_receipt(user_type='user')


# 2.Write a decorator that wraps a function in a try-except block and print an error if error has happened
def catch_errors(func):
    def wrapper(data):
        try:
            func(data)
        except (KeyError) as e:
            print('Found 1 error during execution of your function: ', e)

    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'key': 'bar'})

# 3. Optional: Create a decorator that will check types. It should take a function with arguments and validate inputs with annotations.


def check_types(func):
    def wrapper(*args, **kwargs):
        full_arg_spec = inspect.getfullargspec(func)
        i = 0
        args_list = full_arg_spec.args
        args_type = full_arg_spec.annotations
        for arg in args_list:
            if (type(args[i]) != args_type[arg]):
                raise ValueError('Please check arguments types')
            i += 1
            func(*args, **kwargs)

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)

# Create a function that caches the result of a function, so that if it is called with same argument multiple
# times, it returns the cached result first instead of re-executing the function.
# It`s one of the real task on the project
cache = {}


def memorize(func):
    def wrapper(num):
        if num in cache:
            print('Returned From Cache: ', cache[num])
        else:
            cache[num] = func(num)
            print('Calculated: ', cache[num])
    return wrapper


@memorize
def sum(num: int) -> int:
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum


sum(100)
sum(200)
sum(100)
