class MinStack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, val):
        print(self.getMin())
        if self.getMin() != None:
            min = val if self.getMin() > val else self.getMin()
        else:
            min = val
        self.stack.append({'val': val, 'min': min})
        return True

    def pop(self):
        if self.isEmpty():
            return False
        self.stack.pop()
        return True

    def top(self):
        if self.isEmpty():
            return
        return self.stack[len(self.stack)-1].get('val')

    def isEmpty(self):
        return self.stack == []

    def getMin(self):
        if self.isEmpty():
            return
        print(self.stack[len(self.stack)-1].get('min'))
        return self.stack[len(self.stack)-1].get('min')


minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
minStack.getMin()
minStack.top()
minStack.getMin()
print(123)
