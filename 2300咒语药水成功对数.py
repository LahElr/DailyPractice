r'''
给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，
其中 spells[i] 表示第 i 个咒语的能量强度，potions[j] 表示第 j 瓶药水的能量强度。
同时给你一个整数 success 。
一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。
请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。
'''

import bisect
from typing import Any, List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        spells = sorted(zip(spells,range(n)),key=lambda x:x[0])
        potions.sort(reverse=True)
        pairs = [0 for _ in range(n)]

        # spell升序，potions降序，
        # 如果一个组合成功了，说明更大的spell和更大的potion都必然成功，没必要再算一遍
        # 复杂度是O(NlogN+MlogM+M+N)+O(N)

        scur = 0
        pcur = 0
        while True:
            if scur == n:
                break
            s,si = spells[scur]
            if pcur == m:
                pairs[si] = m
                scur+=1
                continue
            p = potions[pcur]
            v = s*p
            if v<success:
                pairs[si] = pcur
                scur+=1
                continue
            else:
                pcur+=1
                continue
        return pairs
    
    def successfulPairs_bisect(self,spells,potions,success):
        #使用二分查找，不仅空间复杂度降低到O(1)
        #时间复杂度也降低到O(MlogM+NlogM)……本该是这样的……
        #但是用时反而涨了将近30%？
        #因为额外的乘法运算吗？？？
        n = len(spells)
        m = len(potions)
        potions.sort()
        pairs = [0 for _ in range(n)]

        for i,s in enumerate(spells):
            pairs[i] = m-bisect.bisect_left(potions,success,key=lambda x:x*s)
        return pairs

spells = [15,8,19]
potions = [38,36,23]
success = 328

print(Solution().successfulPairs(spells,potions,success))