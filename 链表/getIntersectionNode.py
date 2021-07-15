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
        


listNode1 = generatorNodeList(8, 9)
listNode2 = generatorNodeList(4, 9)
s = Solution()

print(s.getIntersectionNode(listNode1, listNode2))