class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        for i in range(len(str)):
            pre = str[i - 1] if i > 0 else None
            cur = str[i]
            next = str[i + 1] if i < len(str) - 1 else None
        
            if self.is_digit(cur):
                if self.is_digit(pre):
                    stack.

    

    def is_digit(self, s):
        return 0<=s<=9