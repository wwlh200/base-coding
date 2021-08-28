class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A == 0:
            return 0
        result = self.multiply(A>>1,B)

        if A%2==0:
            return result+result
        else:
            return result+result+B

            