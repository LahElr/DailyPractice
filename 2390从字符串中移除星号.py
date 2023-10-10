r"""
有字符串s，包含若干星号符号
在任一步操作中可以：
    选中一个星号
    移除该星号左侧最近的非星号字符和该星号
返回移除所有星号后的字符串
题目保证总可以进行且结果唯一
"""


class Solution:
    def removeStars(self, s: str) -> str:
        rcur = lcur = len(s) - 1
        exist_flags = [True for _ in s]
        while True:
            if lcur < 0 or rcur < 0:
                break
            if not exist_flags[lcur]:
                lcur -= 1
                continue
            if not exist_flags[rcur]:
                rcur -= 1
                continue

            lval = s[lcur]
            rval = s[rcur]
            print(f"{lcur}->{lval}; {rcur}->{rval}")
            if rval != "*":
                lcur -= 1
                rcur -= 1
                continue
            if lval != "*" and rval == "*":
                exist_flags[rcur] = False
                exist_flags[lcur] = False
                lcur -= 1
                rcur -= 1
                continue
            if lval == "*" and rval == "*":
                lcur -= 1
                continue
        return "".join([ch if exist_flags[i] else "" for i, ch in enumerate(s)])
    
    def removeStarsExample(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


s = "erase*****"
s = "leet**cod*e"
s = "abb*cdfg*****x*"
print(Solution().removeStars(s))
