class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','I','U','E','O'}
        lcur = 0
        rcur = len(s)-1
        s = list(s)
        while True:
            if lcur>=rcur:
                break
            lch = s[lcur]
            rch = s[rcur]
            l_is_v = lch in vowels
            r_is_v = rch in vowels
            if l_is_v and not r_is_v:
                rcur-=1
            elif l_is_v and r_is_v:
                s[lcur],s[rcur] = s[rcur],s[lcur]
                lcur+=1
                rcur-=1
            elif not l_is_v and not r_is_v:
                lcur+=1
                rcur-=1
            elif not l_is_v and r_is_v:
                lcur+=1
        return "".join(s)

print(Solution().reverseVowels("hello"))