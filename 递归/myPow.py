class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==1:
            return x
        if n==-1:
            return 1/x
        if n==0:
            return 1
        result = self.myPow(x,n>>1)
        
        if n%2==0:
            return result * result
        else:
            return result * result * x