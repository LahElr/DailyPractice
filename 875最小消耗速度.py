r"""珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。
警卫已经离开了，将在 h 小时后回来。
珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。
每个小时，她将会选择一堆香蕉，从中吃掉 k 根。
如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  
珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/koko-eating-bananas
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from bisect import bisect_left
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r"""
        分割的思路
        """
        # argmin_k(sum([piles[i]//k for i])<=h)
        if len(piles) == h:
            return max(piles)
        if sum(piles) <= h:
            return 1
        if len(piles) == 1:
            return piles[0] // h + 1
        split_counts = [1 for _ in range(len(piles))]
        for _ in range(h - len(piles)):
            i = piles.index(max(piles))
            v = piles[i]
            s = split_counts[i]
            piles[i] = v * s / (s + 1)
            split_counts[i] = s + 1

        return max(piles) // 1 + 1

    def minEatingSpeed_example(self, piles, h):
        r"""如果珂珂在h小时内吃掉所有香蕉的最小速度是每小时k个香蕉，
        则当吃香蕉的速度大于每小时k个香蕉时一定可以在h小时内吃掉所有香蕉，
        当吃香蕉的速度小于每小时k个香蕉时一定不能在h小时内吃掉所有香蕉。
        """
        return bisect_left(
            range(max(piles)),
            -h,
            1,
            key=lambda k: -sum((pile + k - 1) // k for pile in piles),
        )


piles = [3, 6, 7, 11]
h = 8
print(Solution().minEatingSpeed_example(piles, h))
