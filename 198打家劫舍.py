r'''
你是一个专业的小偷，计划偷窃沿街的房屋。
每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，
计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
'''

# lahelr 动态规划
r'''
实例答案使用了滑动窗口存储临时结果，
和我的作答的状态定义略有不同
所以只用保存两个
我的作需要三个
'''

# nums = [2,7,9,3,1]

nums = [1, 10, 1, 1, 10, 1]
# 1,10,2,11,20,12


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # r[i] = max(r[i-2],...r[0]), i init = -1 or -2
        # r[0]=n[0]
        if len(nums) <=2:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[0],nums[1],nums[0]+nums[2])

        # r = [nums[0], nums[1]] + [0 for _ in range(len(nums) - 2)]
        r1,r2,r3 = nums[0],nums[1],nums[0]+nums[2]
        for i in range(3, len(nums)):
            # r[i] = max(r[: i - 1]) + nums[i]
            r1,r2,r3 = r2,r3,max(r1,r2)+nums[i]
        # return max(r[-1], r[-2])
        return max(r2, r3)

    def rob_exp(self, nums) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)

        return second


x = Solution()
print(x.rob(nums))
