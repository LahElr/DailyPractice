r'''
给你一个整数数组 cost ，
其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。
一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算达到楼梯顶部并返回的最低花费。
'''
#lahelr 动态规划

# cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
# cost = [100,1,100]

class Solution(object):
    def __init__(self):
        pass

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        thr = 2
        start_thr = 1
        INF = 999999

        if len(cost)<=start_thr:
            return 0
        if len(cost)==start_thr+1:
            return min(cost)

        sumed_cost = [INF for _ in range(len(cost)+1)]
        # sumed_cost[i] = min cost to reach i-th floor:
        # min(sumed_cost[i-thr]+cost[i-thr],...,sumed_cost[i-1]+cost[i-1])
        
        for _ in range(start_thr+1):
            sumed_cost[_] = 0 # sumed_cost[-1]
        for _ in range(start_thr+1,thr):
            sumed_cost[_] = min(cost[:start_thr+1])
        
        print(sumed_cost)

        for i in range(thr,len(sumed_cost)):
            sumed_cost[i] = min([sumed_cost[i-_]+cost[i-_] for _ in range(1, thr+1)])
        
        print(sumed_cost)

        return sumed_cost[-1]

x = Solution()
print(x.minCostClimbingStairs(cost))