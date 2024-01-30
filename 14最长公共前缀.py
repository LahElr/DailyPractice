from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n= len(strs)
        if n ==0:
            return ""
        elif n == 1:
            return strs[0] 
        m = min(len(s) for s in strs)

        for i in range(m):
            ch = strs[0][i]
            for j in range(1,n):
                if strs[j][i] != ch:
                    return strs[0][:i]
        return strs[0][:m]