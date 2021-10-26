class ListNode:
    def __init__(self, val,  min=None, next=None) -> None:
        self.val = val
        self.min = min
        self.next = next


class MinStack:
    def __init__(self) -> None:
        self.stack = None

    def push(self, val):
        if self.isEmpty():
            self.stack = ListNode(val, val, None)
        else:
            self.stack = ListNode(
                val, val if val < self.stack.min else self.stack.min, self.stack)

    def pop(self):
        if self.isEmpty():
            return False
        self.stack = self.stack.next
        return True

    def top(self):
        if self.isEmpty():
            return
        return self.stack.val

    def isEmpty(self):
        return self.stack == None

    def getMin(self):
        if self.isEmpty():
            return
        return self.stack.min


minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
minStack.getMin()
minStack.top()
minStack.getMin()
print(123)
