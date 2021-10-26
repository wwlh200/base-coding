# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from insert import ListNode, generatorNodeList


class Solution:
    def addAfter(self, head, val):
        ln = head
        while ln.next:
            ln = ln.next
        ln.next = val

    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代
        #  pre = None
        #  cur = head
        #  while cur:
        #      next = cur.next
        #      cur.next = pre
        #      pre = cur
        #      cur = next
        #  return pre
        # 递归
        # if not head or not head.next:
        #     return head
        # ret = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None

        # return ret
        # 双指针
        pre = None
        cur = None

        while head:
            next = head.next
            cur = head
            cur.next = pre
            pre = cur
            head = next

        return pre


s = Solution()

# 初始化单链表
listNode1 = generatorNodeList(1, 4)
s.addAfter(listNode1, ListNode(4))
print(listNode1)
listNode2 = s.reverseList(listNode1)

print(listNode2)
