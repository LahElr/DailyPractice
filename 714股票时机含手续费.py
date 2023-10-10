r"""给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        l = len(prices)
        if l <= 1:
            return 0
        min_buy_price = prices[0] + fee  # 若有，则其可能的最低的入手价格？
        profit = 0
        for i, price in enumerate(prices[1:]):
            i += 1
            if price < min_buy_price - fee:
                # 入手（可能
                min_buy_price = price + fee
            elif price > min_buy_price:
                # 出手（可能
                profit += price - min_buy_price
                min_buy_price = price  # 同时保留撤回操作的可能
            else:
                # 不够低到在此处入手，也不够高到可以出手
                pass
        return profit


prices = [1, 3, 7, 5, 10, 3]
fee = 3
print(Solution().maxProfit(prices, fee))
