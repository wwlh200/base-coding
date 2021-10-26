# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from insert import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        d = set()
        while head:
            if head in d:
                return True
            else:
                d.add(head)

            head = head.next
        return False


# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         if head == None or head.next == None:
#             return False

#         slow = head
#         fast = head


#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if fast == slow:
#                 return True
#         return False
