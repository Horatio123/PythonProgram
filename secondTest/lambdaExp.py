from functools import reduce

add = lambda x, y: x + y
product = lambda x, y: x * y

print(add(3, 4))
print(product(5, 8))

my_list = [3, 4, 7, 9]
my_list2 = [6, 3, 5, 9]

a = map(lambda x: x * 2, my_list)
print(list(a))
b = map(lambda x, y: x + y, my_list, my_list2)
print(list(b))
c = filter(lambda x: x % 2 == 0, my_list)
print(list(c))
d = filter(lambda x: True if x >= 5 else False, my_list)
print(list(d))
e = reduce(lambda x, y: x + y, my_list)
print(e)
