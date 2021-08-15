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

    def dequeue(self):
        if self.length == 0:
            return
        self.length -= 1
        self.head += 1
        self.entries = self.entries[self.head:]
        return self.entries[self.head]

    def peek(self):
        return self.entries[0]  # 直接返回队列的队首元素

    def print(self):
        print(self.entries)


class ListNodeQueue:
    def __init__(self):
        self.entries = None  # 表示队列内的参数
        self.size = 0  # 表示队列的长度

    def enqueue(self, item):
        self.size += 1
        if not self.entries:
            self.entries = ListNode(item)
            return
        ln = self.entries
        while ln.next:
            ln = ln.next
        ln.next = ListNode(item)

    def dequeue(self):
        if self.size == 0:
            return
        self.size -= 1
        ret = self.entries.val
        self.entries = self.entries.next
        return ret

    def peek(self):
        return self.entries.val  # 直接返回队列的队首元素

    def print(self):
        print(self.entries)


queue = ListNodeQueue()
queue.enqueue(12)
queue.enqueue(34)
queue.enqueue("abd")
queue.enqueue(999)
queue.print()
print(queue.dequeue())
queue.print()
