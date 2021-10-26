class Solution:
     # 数字存一个变量，字符串存一个变量，遇到[入栈,遇到]出栈累加
    def decodeString(self, s: str) -> str:
        stack=[]
        num = 0
        res =""
        for char in s:
            if "0"<=char<="9":
                num=num*10+int(char)
            elif char=="[":
                stack.append([num,res])
                num=0
                res=""
            elif char == "]":
                sub_num,sub_res=stack.pop()
                res=sub_res+sub_num*res
            else:
                res+=char

        return res


s=Solution()
print(s.decodeString("abc3[cd]xyz"))