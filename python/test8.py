class Student(object):
    def __init__(self) -> None:
        super().__init__()
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be an integer!")
        if score < 0 or score > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = score


s = Student()

print(s.score)
s.score = 20
print(s.score)


class Screen(object):
    def __str__(self) -> str:
        return '123'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

s=Screen()
print(s)