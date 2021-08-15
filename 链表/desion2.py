class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# def generator_ln(m, n):
#     for i in range(m,n):
#         ListNode

class myListNode:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # 哨兵节点

    # 在中间插入
    def add_in(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0
        self.size += 1

        ln = self.head
        new = ListNode(val)
        for _ in range(index):
            ln = ln.next
        new.next = ln.next
        ln.next = new
    # 在前面插入

    def add_before(self, val):
        self.add_in(0, val)
    # 在后面插入

    def add_after(self, val):
        self.add_in(self.size, val)
    # 在中间删除

    def delete_in(self, index):
        if index < 0 or index >= self.size:
            return

        ln = self.head
        self.size -= 1
        for _ in range(index):
            ln = ln.next
        if ln.next:
            ln.next = ln.next.next

    # 删除第一个

    def delete_before(self):
        if self.head:
            self.size -= 1
            self.head = self.head.next
    # 删除最后一个

    def delete_after(self):
        ln = self.head
        while ln.next:
            ln = ln.next
        self.size -= 1
        ln = None

    # 获取链表第i个节点

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        ln = self.head
        for _ in range(index+1):
            ln = ln.next
        return ln.val


s = myListNode()
s.add_after(1)
s.add_after(2)
s.add_before(0)
s.add_in(3, 2.5)
s.add_after(3)


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # s = set()
        # while head:
        #     if head in s:
        #         return True
        #     else:
        #         s.add(head)
        #     head = head.next
        # return False
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def detectCycle(self, head):
        # s = set()
        # while head:
        #     if head in s:
        #         return head
        #     else:
        #         s.add(head)
        #     head = head.next
        # return None
        if not head:
            return None

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head:
                    if head == slow:
                        return head
                    head = head.next
                    slow = slow.next
        return None
