class Publish:
    def __init__(self):
        self.subs = []

    def add(self, sub):
        self.subs.append(sub)

    def notify(self, msg):
        for sub in self.subs:
            sub.print(msg)


class Sub:
    def __init__(self, name):
        self.name = name

    def print(self,msg):
          print(f"{self.name}{msg}")


s1=Sub("zhangsan")
s2=Sub("lisi")

p=Publish()

p.add(s1)
p.add(s2)

p.notify("zuishuai")