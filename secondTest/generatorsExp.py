def x_fun():
    n = 1
    print("---------", n)
    yield n
    n += 1
    print("---------", n)
    yield n
    n += 1
    print("---------", n)
    yield n


x = x_fun()
print(next(x))
print(next(x))
print(next(x))
# print(next(x))
print("=========")


def y_fun(list_input):
    for i in list_input:
        yield i


a = range(10)
y = y_fun(a)
for num in a:
    print(next(y))
