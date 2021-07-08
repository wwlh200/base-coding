def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(36))


def fib_total(n, ret1, ret2):
    if n == 1:
        return ret2
    return fib_total(n - 1, ret2, ret1 + ret2)


print(fib_total(35, 1, 1))
