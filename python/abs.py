from functools import reduce

x = abs
print(x(-10))

abs = 10
print(abs)


def add(x, y, s):
    return s(x) + s(y)


def s(value):
    return value + 10


print(add(1, 2, s))


def f(x):
    return f1


L = [1, 2, 3, 4, 5]
r = filter(f, L)
print(r)
