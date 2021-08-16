class MyCircularQueue:
    def __init__(self, k: int):
        # 一个固定大小的数组，用于保存循环队列的元素。
        self.queue = ['0']*k
        # 一个整数，保存队首 head 的索引
        # self.tail=(self.head+self.count-1)%self.capacity
        self.head = -1
        # 循环队列当前的长度，即循环队列中的元素数量。使用 hadIndex 和 count 可以计算出队尾元素的索引，因此不需要队尾属性。
        self.count = 0
        # capacity：循环队列的容量，即队列中最多可以容纳的元素数量。
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[(self.head+self.count) % self.capacity] = value
            self.count += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.head = (self.head+1) % self.capacity
            self.count -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.head+self.count-1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


circularQueue = MyCircularQueue(8)  # 设置长度为 3
circularQueue.enQueue(8)   # 返回 true
circularQueue.enQueue(3)   # 返回 true
circularQueue.enQueue(9)   # 返回 true
circularQueue.enQueue(5)   # 返回 true
circularQueue.deQueue()   # 返回 true
circularQueue.deQueue()   # 返回 true
circularQueue.isEmpty()   # 返回 true
circularQueue.isEmpty()   # 返回 true
circularQueue.Rear()   # 返回 true
circularQueue.Rear()   # 返回 true
circularQueue.deQueue()   # 返回 true
