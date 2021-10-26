class Solution:
    # n=0
    # n=n-1
    def countDigitOne(self, n: int, num=0) -> int:
        return 10 ** (self.countDigitOne-1) + 10 * self.f(i-1) if i else 0


s = Solution()
print(s.countDigitOne(65536))
