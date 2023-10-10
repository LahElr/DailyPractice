r'''
给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，
使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。
'''
#lahelr 贪心，简单遍历，记忆前两个，使其尽可能小
# nums = [1,2,3,4,5]
# nums = [20,100,10,95,90,13]
# nums = [20,100,10,12,5,13]
nums = [2,1,5,0,4,6]
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        bigger_num_ahead_flags = [False for _ in range(len(nums))]
        big_num = nums[-1]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]< big_num:
                bigger_num_ahead_flags[i] = True
            else:
                big_num = nums[i]

        small_num = float('inf')
        for i in range(len(nums)):
            if bigger_num_ahead_flags[i]:
                if nums[i]< small_num:
                    small_num = nums[i]
                elif nums[i]>small_num:
                    return True
        return False

x = Solution()
print(x.increasingTriplet(nums))