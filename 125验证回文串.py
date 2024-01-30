class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s)-1

        while lp<rp:
            if not s[lp].isalnum():
                lp+=1
                continue
            if not s[rp].isalnum():
                rp-=1
                continue
            # print(lp,s[lp],s[rp],rp)
            if not s[rp].lower() == s[lp].lower():
                return False
            else:
                lp+=1
                rp-=1
        return True