# def now():
#     print("2020-06-11")


# f = now

# f()

# print(f.__name__)


def log(func):
    def wrapper():
        print("12345")
        return func()

    return wrapper


@log
def now():
    print("2020-06-11")


now()
