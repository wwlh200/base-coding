# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from insert import generatorNodeList


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """
        # 哈希表
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next

        while headB:
            if headB in s:
                return headB
            headB = headB.next
        return None
        """
        head1 = headA
        head2 = headB
        """
            1、相交相等
            2、相交不相等 a+c+b=b+c+a
            3、不相交相等
            4、不相交不等 m+n=n+m
        """
        while head1 != head2:
            head1 = head1.next if head1 else headB
            head2 = head2.next if head2 else headA
        return head1


listNode1 = generatorNodeList(8, 9)
listNode2 = generatorNodeList(4, 9)
s = Solution()

print(s.getIntersectionNode(listNode1, listNode2))
