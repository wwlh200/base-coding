class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class ArrayQueue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        return self.queue[0]

    def print(self):
        print(self.queue)

class ListNodeQueue:
    def __init__(self) -> None:
        self.queue = None
        self.size = 0

    def enqueue(self, item):
        self.size += 1
        new = ListNode(item)
        if not self.queue:
            self.queue = new
            return
        ln = self.queue
        while ln.next:
            ln = ln.next
        ln.next = new

    def dequeue(self):
        if self.size == 0:
            return
        self.size -= 1
        self.queue = self.queue.next

    def peek(self):
            return self.queue.val

    def print(self):
        print(self.queue)

queue1 = ListNodeQueue()
queue1.enqueue(44)
queue1.enqueue(99)
queue1.enqueue("BB")
queue1.print()
print(queue1.dequeue())
print(queue1.peek())