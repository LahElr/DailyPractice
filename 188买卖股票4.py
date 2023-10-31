r"""
给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""


import heapq
from typing import List


class Interval:
    r"""
    作者：未加标签
    链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/2476534/zen-yao-you-ren-yong-zui-xiao-dui-shen-z-z2xe/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""

    r'''
    是个链表
    '''

    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.length = high - low
        self.merge2next = self.merge2prev = self.length
        self.mn = self.length
        self.option = 0  # 1：向前合并，2：向后合并，初始设为0但不会是0，因为总会让他向前或者向后
        self.next = self.prev = None

    def update(self):
        self.length = self.high - self.low
        self.merge2next = self.merge2prev = self.length
        x2, y2 = self.low, self.high
        if self.prev:
            x1, y1 = self.prev.low, self.prev.high
            if x1 <= y1 <= x2 <= y2:
                self.merge2prev = 0
            elif x1 <= x2 <= y1 <= y2:
                self.merge2prev = y1 - x2
        if self.next:
            x3, y3 = self.next.low, self.next.high
            if x2 <= y2 <= x3 <= y3:
                self.merge2next = 0
            elif x2 <= x3 <= y2 <= y3:
                self.merge2next = y2 - x3
        # 如果向前合并和向后合并一样，那就如果前面有就向前合并，前面没有就向后合并
        if self.merge2prev <= self.merge2next and self.prev:
            self.mn, self.option = self.merge2prev, 1
        elif self.merge2prev >= self.merge2next and self.next:
            self.mn, self.option = self.merge2next, 2

    def __lt__(self, other):
        return self.mn < other.mn

    def delete(self):
        p = self.prev
        n = self.next
        if self.option == 1:
            p.high = max(self.high, p.high)
            # 不能直接 p.low = min(self.low, p.low)，因为当前这个是要被删除的，
            # 如果前一个的low比当前的大，合并之后的的high只能还是前一个的high
            # 下同
            p.low = min(self.low, p.low) if p.high == self.high else p.low
            p.next = n
            if n:
                n.prev = p
                n.update()
            p.update()
        elif self.option == 2:
            n.low = min(self.low, n.low)
            n.high = max(self.high, n.high) if n.low == self.low else n.high
            n.prev = p
            if p:
                p.next = n
                p.update()
            n.update()


class AnotherSolution:
    r"""
    作者：未加标签
    链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/2476534/zen-yao-you-ren-yong-zui-xiao-dui-shen-z-z2xe/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        is_increase = False  # 是否在增长区间
        a = []
        # high = low = 0
        for i in range(1, n):
            x, y = prices[i - 1], prices[i]
            if y > x:
                ans += y - x
                if not is_increase:  # x是最低点。当前不是在增长，那x是最低点，从x开始增长
                    is_increase = True
                    low = x
                if i == n - 1:
                    a.append(Interval(low, y))
            else:
                if is_increase:  # x是最高点
                    is_increase = False
                    a.append(Interval(low, x))

        cnt = len(a)
        if cnt == 0:  # 没有一个增长区间，返回0
            return ans

        for i in range(cnt):
            a[i].next = a[i + 1] if i < cnt - 1 else None
            a[i].prev = a[i - 1] if i > 0 else None
            a[i].update()

        heapq.heapify(a)

        while cnt > k:
            interval = heapq.heappop(a)
            mn = interval.mn
            ans -= mn
            interval.delete()
            heapq.heapify(a)
            cnt -= 1
        return ans


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        k = min(len(prices) // 2, k)

        have = [[0 for j in range(k + 1)] for i in range(len(prices))]
        havent = [[0 for j in range(k + 1)] for i in range(len(prices))]

        # have[i][j] = max(have[i-1][j], havent[i-1][j]-price[i])
        # havent[i][j] = max(have[i-1][j-1]+price[i],havent[i-1][j])

        have[0][0] = -prices[0]
        # havent[0][0] = 0
        for j in range(1, k + 1):
            have[0][j] = -10000
            havent[0][j] = -10000

        for i in range(1, len(prices)):
            have[i][0] = max(have[i - 1][0], havent[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                have[i][j] = max(have[i - 1][j], havent[i - 1][j] - prices[i])
                havent[i][j] = max(have[i - 1][j - 1] + prices[i], havent[i - 1][j])

        # print(have)
        # print(havent)
        return max(havent[-1])

    def official_one_dimension_solution(self, k, prices):
        r"""https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/537731/mai-mai-gu-piao-de-zui-jia-shi-ji-iv-by-8xtkp/"""
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [0] * (k + 1)
        sell = [0] * (k + 1)

        buy[0], sell[0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[i] = sell[i] = float("-inf")

        for i in range(1, n):
            buy[0] = max(buy[0], sell[0] - prices[i])
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j] - prices[i])
                sell[j] = max(sell[j], buy[j - 1] + prices[i])

        return max(sell)


# prices = [3,5,3,4,1,4,5,0,7,8,5,6,9,4,1]
prices = [3, 2, 6, 5, 0, 3]
k = 2
print(Solution().maxProfit(k, prices))
