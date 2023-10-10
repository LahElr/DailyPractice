r"""泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。"""


from collections import deque


class Solution:
    def tribonacci(self, n: int) -> int:
        #lahelr 这是题目限定n<=37的结果
        res = [
            0,
            1,
            1,
            2,
            4,
            7,
            13,
            24,
            44,
            81,
            149,
            274,
            504,
            927,
            1705,
            3136,
            5768,
            10609,
            19513,
            35890,
            66012,
            121415,
            223317,
            410744,
            755476,
            1389537,
            2555757,
            4700770,
            8646064,
            15902591,
            29249425,
            53798080,
            98950096,
            181997601,
            334745777,
            615693474,
            1132436852,
            2082876103,
        ]
        l = len(res)
        if n < len(res):
            return res[n]
        queue = deque(res[-3:])
        del res
        for i in range(l, n + 1):
            val = sum(queue)
            queue.popleft()
            queue.append(val)
        return queue.pop()


print(Solution().tribonacci(37))
