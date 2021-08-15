from insert import ListNode, generatorNodeList


class Solution:
    def addAfter(self, head, val):
        ln = head
        while ln.next:
            ln = ln.next
        ln.next = val

    def isPalindrome(self, head: ListNode) -> bool:
        nums, nums2 = [], []
        while head:
            nums.append(head.val)
            nums2.insert(0, head.val)
            head = head.next

        if nums == nums2:
            return True
        return False


s = Solution()
ln = ListNode(1)
# 初始化单链表
s.addAfter(ln, ListNode(2))
s.addAfter(ln, ListNode(2))
s.addAfter(ln, ListNode(1))
s.isPalindrome(ln)
print(ln)
