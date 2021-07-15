from insert import generatorNodeList

class ListNode(object):
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class MyListNode(object):
    def __init__(self, ln) -> None:
        super().__init__()
        self.ln = ln

    # 获取链表中第 index 个节点的值。如果索引无效，则返回-1。
    def get(self, index):
        head = self.ln
        i = 0
        while head.next:
            if i == index:
                return head.val
            head = head.next
            i += 1

        return -1

    # 在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
    def addAtHead(self, val):
        head = self.ln
        new = ListNode(val)
        new.next = head
        head = new
        return head

    # 将值为 val 的节点追加到链表的最后一个元素。
    def addAtTail(self, val):
        head = self.ln
        ln = head
        new = ListNode(val)
        while head:
            if head.next == None:
                head.next = new
                new.next = None
                break
            head = head.next
        head = ln
        return head
    # 在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。
    # 如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。

    def addAtIndex(self, index, val):
        i = 0
        head = self.ln
        ln = head
        new = ListNode(val)
        # 链表为空
        if head == None:
            head = new
            return head
        # index<0
        if index < 0:
            new.next = head
            head = new
            return head
        
        while head:
            if i+1 == index and  head.next and head.next.next:
                new.next = head.next
                head.next = new
                break
            if i == index:
                head.next=new
            i += 1
            head = head.next
            
        head = ln
        return head

    # 如果索引 index 有效，则删除链表中的第 index 个节点。
    def deleteAtIndex(self, index):
        i = 0
        head = self.ln
        ln = head
        while head.next:
            if i+1 == index:
                head.next = head.next.next
                break
            i += 1
            head = head.next
        head = ln
        return head


listNode1 = generatorNodeList()

myLN = MyListNode(listNode1)
ln = myLN.addAtIndex(2, 'x')
print(ln)
