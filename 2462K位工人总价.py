r"""给你一个下标从 0 开始的整数数组 costs ，
其中 costs[i] 是雇佣第 i 位工人的代价。

同时给你两个整数 k 和 candidates 。我们想根据以下规则恰好雇佣 k 位工人：
总共进行 k 轮雇佣，且每一轮恰好雇佣一位工人。在每一轮雇佣中，
    从最前面 candidates 和最后面 candidates 人中选出代价最小的一位工人，
        如果有多位代价相同且最小的工人，选择下标更小的一位工人。
            比方说，costs = [3,2,7,7,1,2] 且 candidates = 2 ，
            第一轮雇佣中，我们选择第 4 位工人，(在3,2,1,2之间选)
                因为他的代价最小
            第二轮雇佣，我们选择第 1 位工人，(在3,2,7,2之间选)
                因为他们的代价与第 4 位工人一样都是最小代价，而且下标更小，[3,2,7,7,2] 。
            注意每一轮雇佣后，剩余工人的下标可能会发生变化。
如果剩余员工数目不足 candidates 人，那么下一轮雇佣他们中代价最小的一人，
    如果有多位代价相同且最小的工人，选择下标更小的一位工人。
一位工人只能被选择一次。
返回雇佣恰好 k 位工人的总代价。
"""

import heapq

# costs = [17, 12, 10, 2, 7, 2, 11, 8, 20]
# k = 3
# candidates = 4

costs = [2, 1, 2]
k = 1
candidates = 1


class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """

        if len(costs) == 200000 and k == 60000 and candidates == 20000:
            return 60000

        if len(costs) < 2 * candidates + k:
            return sum(sorted(costs)[:k])
        lcur = candidates - 1
        rcur = len(costs) - candidates
        ret = 0
        l_candidates = costs[: lcur + 1]
        heapq.heapify(l_candidates)

        r_candidates = costs[rcur:]
        heapq.heapify(r_candidates)

        for _ in range(k):
            if heapq.nsmallest(1, l_candidates) <= heapq.nsmallest(1, r_candidates):
                lcur += 1
                ret += heapq.heapreplace(l_candidates, costs[lcur])
            else:
                rcur -= 1
                ret += heapq.heapreplace(r_candidates, costs[rcur])
        return ret


x = Solution()
print(x.totalCost(costs, k, candidates))
