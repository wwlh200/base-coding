class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if int(n % 2) == 1 or n == 0:
            return False

        return self.isPowerOfTwo(n/2)

s = Solution()
print(s.isPowerOfTwo(10))
