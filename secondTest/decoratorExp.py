from time import time


def decorator_func(func):
    def wrapper_func():
        print('x' * 20)
        func()
        print('y' * 20)

    return wrapper_func


# def say_hello():
#     print("hello python")
#
#
# hello = decorator_func(say_hello)
# hello()

@decorator_func
def say_hello():
    print("hello python3")


print('decorator_func:')
say_hello()


# with input args
def decorator_divide(func):
    def wrapper_func(a, b):
        print('divide ', a, ' and ', b)
        return func(a, b)
    return wrapper_func


@decorator_divide
def divide(a, b):
    return a / b


print('decorator_divide:')
print(divide(9, 3))


def timing(func):
    def wrapper_fun(*args, **kwargs):
        start = time()
        print(start)
        result = func(*args, **kwargs)
        end = time()
        print(end)
        print('elapsed time: {}'.format(end - start))
        return result

    return wrapper_fun


@timing
def my_sum(num):
    sum = 0
    for i in range(num):
        sum += i
    return sum


print('timing:')
my_sum(9999)
