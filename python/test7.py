from types import MethodType


class Student(object):
    __slots__=('name','age')


def set_age(self, age):
    self.age = age


s = Student()
s.name = "王维林"
Student.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)
