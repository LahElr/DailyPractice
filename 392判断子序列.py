r'''
给定字符串s和t，判断s是否为t的子序列
另外，若s极多，但t始终相同。则何如？
'''

r'''
双指针扫过去就行了
多个s的话就挨个走，反正每步t指针都要前进，t到头了，s没到头的就是不行的
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        scur = 0
        tcur = 0
        slen = len(s)
        tlen = len(t)
        if tlen < slen:
            return False
        while True:
            if scur>=slen:
                return True
            if tcur >= tlen:
                return False
            sval = s[scur]
            tval = t[tcur]
            if sval == tval:
                scur+=1
            tcur+=1
        return None

s = 'axc'
t='ahbgdc'

print(Solution().isSubsequence(s,t))