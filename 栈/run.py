from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack, sum = [], 0
        for char in ops:
            try:
                num = int(char)
                stack.append(num)
            except:
                if char == 'C':
                    stack.pop()
                elif char == 'D':
                    stack.append(stack[-1]*2)
                else:
                    stack.append( stack[-1] + stack[-2])

        for char in stack:
            sum += char

        return sum


s = Solution()
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))

