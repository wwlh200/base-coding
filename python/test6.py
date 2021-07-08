class Student(object):
    def __init__(self, **kw) -> None:
        super().__init__()
        self.name = kw["name"]

    name = "20"


s = Student(name="BoB")
print(s.name)
s.age = 30
print(s.age)
