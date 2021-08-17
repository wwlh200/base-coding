class Solution:
    def __init__(self) -> None:
        self.stack = []

    def isValid(self, s: str) -> bool:
        if (len(s) < 2):
            return False
        for char in s:
            if char == '(':
                self.stack.append(')')
            elif char == '[':
                self.stack.append(']')
            elif char == '{':
                self.stack.append('}')
            elif len(self.stack) == 0 or self.stack.pop() != char:
                return False

        if len(self.stack) > 0:
            return False

        return True


s = Solution()

s.isValid("((")
print(123)
