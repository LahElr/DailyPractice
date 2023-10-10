r"""
给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。
"""

#lahelr 双指针，前缀和

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3


class Solution(object):
    def __init__(self):
        pass

    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # sums[i] = sums[i-1]+nums[i]
        lsum = 0
        rsum = 0
        lcur = 0
        rcur = 0
        ret = 0
        nums = [1 if _==0 else 0 for _ in nums]
        while True:
            rcur += 1
            rsum += nums[rcur-1]
            # print(rcur, rsum,end=" - ")

            while True:
                if rsum - k > lsum:
                    lcur += 1
                    lsum += nums[lcur-1]
                else:
                    break
            # print(lcur, lsum)

            if rcur - lcur > ret:
                ret = rcur - lcur
            if rcur >= len(nums):
                break

        return ret


# print([sum(nums[:i+1]) for i in range(len(nums))])

x = Solution()
print(x.longestOnes(nums, K))
