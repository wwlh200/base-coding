from collections.abc import Iterable

d = {"a": 1, "b": 2, "c": 3}
if isinstance(d, Iterable):
    for key, value in d.items():
        print(value)

print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x*x)
print(L)