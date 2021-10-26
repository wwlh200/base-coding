"""
结束条件：n=1 n=2
缩小范围：n*fn(n-1)
"""


def avg(n):
    if n == 1 or n == 2:
        return n

    return n * avg(n - 1)


print(avg(5))

"""
迭代
存储上一次结果
"""


def avg2(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
print(avg2(6))