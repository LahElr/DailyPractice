r"""给定一个整数数组 temperatures ，表示每天的温度，
返回一个数组 answer ，
其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
如果气温在这之后都不会升高，请在该位置用 0 来代替。
"""

#lahelr 遇见低温放进栈

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
temperatures = [30, 40, 50, 60]


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        previous_low_i = []  # must be descending
        ret = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            while (
                len(previous_low_i) > 0
                and temperatures[previous_low_i[-1]] < temperatures[i]
            ):
                prev_ind = previous_low_i.pop()
                ret[prev_ind] = i - prev_ind
                
            previous_low_i.append(i)
        return ret

x = Solution()
print(x.dailyTemperatures(temperatures))
