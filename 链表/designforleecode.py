class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。
如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
"""


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # 哨兵节点

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        new = ListNode(val)
        new.next = pred.next
        pred.next = new

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        self.size -= 1

        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next
