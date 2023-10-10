r"""给你一个字符数组 chars ，请使用下述算法压缩：

从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：

如果这一组长度为 1 ，则将字符追加到 s 中。
否则，需要向 s 追加字符，后跟这一组的长度。
压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

请在 修改完输入数组后 ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        def reverse(left,right):
            while left<right:
                chars[left],chars[right] = chars[right],chars[left]
                left+=1
                right-=1
        
        l = len(chars)
        wcur = 0
        unreadcur = 0
        for rcur in range(l):
            if rcur == l-1 or chars[rcur]!=chars[rcur+1]:
                chars[wcur] = chars[rcur]
                wcur+=1
                num = rcur-unreadcur + 1
                if num>1:
                    wlcur = wcur
                    while num>0:
                        chars[wcur]= str(num%10)
                        wcur+=1
                        num = num//10
                    reverse(wlcur,wcur-1)
                unreadcur = rcur+1
        return wcur

chars = ["a", "a", "b", "b", "c", "c", "c"]
x = Solution().compress(chars)
print(chars)
print(x)
print(chars[:x])
