r'''
给定一个只包括 '(', ')', '{', '}', '[', ']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {'(':0, ')':1, '{':2, '}':3, '[':4, ']':5}
        for ch in s:
            if mapper[ch]%2:
                if len(stack) == 0 or stack[-1] != mapper[ch]-1:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(mapper[ch])
        return len(stack)==0
    
s = "]"
print(Solution().isValid(s))
