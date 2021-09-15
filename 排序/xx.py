from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = None
        nums.sort()
        length = len(nums)
        if length == 3:
            return nums[0]+nums[1]+nums[2]

        for i in range(1, length-1):
            start = 0
            end = length-1
            while start < i < end:
                sum = nums[start]+nums[i]+nums[end]-target
                if not diff:
                    diff=sum
                else:
                    diff = diff if abs(diff) < abs(sum) else sum
                if sum == 0:
                    return target
                elif sum < 0:
                    start += 1
                elif sum > 0:
                    end -= 1

        return target+diff


s = Solution()

s.threeSumClosest([-1, 2, 1, -4], 1)
