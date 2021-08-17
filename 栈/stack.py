class Stack:
    def __init__(self, capacity) -> None:
        self.stack = []
        self.capacity = capacity

    def push(self, val):
        if self.isFull():
            print('栈满了')
            return False
        self.stack.append(val)
        return True

    def pop(self):
        if self.isEmpty():
            print('栈空了')
            return False
        self.stack.pop()
        return True

    def top(self):
         if self.isEmpty():
            print('栈空了')
            return -1
         return self.stack[len(self.stack-1)]

    def isEmpty(self):
        return self.stack == []

    def isFull(self):
        return len(self.stack) == self.capacity
