class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class ArrayQueue:
    def __init__(self):
        self.entries = []  # 表示队列内的参数
        self.length = 0  # 表示队列的长度
        self.head = 0  # 表示队列头部位置

    def enqueue(self, item):
        self.entries.append(item)
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return False
        self.length -= 1
        self.head += 1
        self.entries.pop(0)
        return True

    def peek(self):
        return self.entries[0]  # 直接返回队列的队首元素

    def print(self):
        print(self.entries)


class ListNodeQueue:
    def __init__(self):
        self.head = None  # 表示队首的参数
        self.tail = None  # 表示队尾的参数

    def enqueue(self, item):
        new = ListNode(item)
        if self.is_empty():
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def dequeue(self):
        if self.is_empty():
            print("空队列无法出队")
        else:
            self.head = self.head.next

    def is_empty(self):
        return not self.head

    def peek(self):
        return self.head.val

    def print(self):
        print(self.head)


queue = ArrayQueue()
queue.enqueue(12)
queue.enqueue(34)
queue.enqueue("abd")
queue.enqueue(999)
queue.print()
print(queue.dequeue())
queue.print()
