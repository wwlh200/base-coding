class Student(object):
    def __init__(self, **kw):
        self.__name = kw["name"]
        self.store = kw["store"]

    def print_store(self):
        print(self.store)

    def print_name(self):
        print(self.__name)


s1 = Student(name="王维林123", store="20")
s2 = Student(name="wanng", store="30")

s1.print_store()
s2.print_name()

s1.name1 = 123


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender
        if gender not in ("male", "female"):
            print("测试失败！")
        else:
            print("测试成功！")


bart = Student("Bart", "male")


class Teacher(Student):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def print_teacher(self, name):
        print(name)

    def get_gender(self):
        return f"123{self.__gender}"


teacher = Teacher("Bart", "male")
print(teacher.get_gender())

teacher.print_teacher("waw")


def run_twice(a):
    print(a.get_gender())
    print(a.get_gender())

run_twice(bart)


class Timer(object):
    def run(self):
        print('Start...')

print(type('123'))

print(len(dir(teacher)))