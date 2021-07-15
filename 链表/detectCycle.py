# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from insert import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> bool:
        d = set()
        while head:
            if head in d:
                return head
            else:
                d.add(head)
            head = head.next
        return None


class Solution:
    def detectCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                # 只要把其中一个指针放回头节点位置，另外一个指针保持在首次相遇点，两个指针每次向前走1步，那么，他们最终相遇的节点，就是入环节点
                meetNode = slow
                start = head
                while start != meetNode:
                    start, meetNode = start.next, meetNode.next
                return meetNode
        return None
