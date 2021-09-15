from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": lambda x, y: int(x + y),
            "-": lambda x, y: int(x - y),
            "*": lambda x, y: int(x * y),
            "/": lambda x, y: int(x / y),   # 需要注意 python 中负数除法的表现与题目不一致
        }

        stack = []
        for char in tokens:
            try:
                stack.append(int(char))
            except:
                stack.append(op_to_binary_fn[char](stack.pop(-2), stack.pop()))
        return stack[0]


s = Solution()
s.evalRPN(["4", "13", "5", "/", "+"])
