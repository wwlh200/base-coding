from typing import List


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyListNode:
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def insert(self, index, val):
        if index > self.size():
            return
        if index < 0:
            index = 0
        self.size += 1
        ln = self.head
        for _ in range(index):
            ln = ln.next
        new = ListNode(val)
        new.next = ln.next
        ln.next = new

    def delete(self, index):
        if index < 0 or index > self.size:
            return
        ln = self.head
        self.size -= 1
        for _ in range(index):
            ln = ln.next
        ln = ln.next.next

    def deleteNode(self, node):
        ln = self.head
        index = 0
        while ln:
            if ln == node:
                break
            index += 1
            ln = ln.next
        
        for _ in range(index):
            ln = ln.next
        ln = ln.next.next


class Solution:
    # 26. 删除有序数组中的重复项
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        slow = fast = 1
        while fast < n:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast+1
        return slow

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        ans = 0
        while left < right:
            area = (right-left)*min(height[left], height[right])
            ans = max(ans, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans

    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

    def findRepeatNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)
