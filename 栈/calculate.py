class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = 1
        # 将符号和数字一起存储
        for char in s:
            if "0" <= char <= "9":
                num = num * 10 + int(char)
            elif char == '+':
                res += sign * num
                num = 0
                sign = 1
            elif char == '-':
                res += sign * num
                num = 0
                sign = -1
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ')':
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res
