from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = nums1[0:m]+nums2
        return self.quick_sort(nums)

    def quick_sort(self, arr):
        length = len(arr)
        if length <= 1:
            return arr
        mid = arr.pop(0)

        left, right = [], []
        for value in arr:
            left.append(value) if value < mid else right.append(value)

        return self.quick_sort(left)+[mid]+self.quick_sort(right)


s = Solution()
s.merge([1, 2, 3, 0, 0, 0],
        3,
        [2, 5, 6],
        3)
print(s.merge([1, 2, 3, 0, 0, 0],
        3,
        [2, 5, 6],
        3))