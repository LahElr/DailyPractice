r"""
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。
可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组 flowerbed 表示花坛，
由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。
另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？
能则返回 true ，不能则返回 false 。

题目保证n<=len(flowerbed)，且数据中不存在相邻的两个1
"""


from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lcur = -2 # the index of last 1
        for rcur, v in enumerate(flowerbed):
            if v == 1:
                lcur = rcur
            else:
                if rcur - lcur > 2:
                    lcur = rcur - 1
                    n -= 1
        # equal to appending a virtul 0 to `flowerbed`
        rcur+=1
        if rcur-lcur >2:
            n-=1
        return n <= 0


data = [1, 0, 0, 0, 1, 0, 0]
n = 2
print(Solution().canPlaceFlowers(data, n))
