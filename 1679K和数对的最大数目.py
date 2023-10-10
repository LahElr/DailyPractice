r'''给你一个整数数组 nums 和一个整数 k 。
每一步操作中，你需要从数组中选出和为 k 的两个整数，并将它们移出数组。
返回你可以对数组执行的最大操作数。
'''

#lahelr 排序，然后从左右双指针

nums = [3,1,3,4,3]
k = 6

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        inf = float('inf')

        rcur = len(nums)-1
        lcur = 0
        ret = 0
        nums = sorted(nums)

        while True:
            # print(lcur,nums[lcur],rcur,nums[rcur])
            if lcur>=rcur:
                break
            x = nums[lcur]+nums[rcur]
            if x == k:
                lcur+=1
                rcur-=1
                ret+=1
                continue
            elif x<k:
                lcur+=1
                continue
            elif x>k:
                rcur-=1
                continue

        return ret

x = Solution()
print(x.maxOperations(nums,k))