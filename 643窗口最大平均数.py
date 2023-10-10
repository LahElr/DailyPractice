r'''找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数
容许10^-5内的误差，题目保证k<=n
'''

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n<=k:
            return sum(nums)/n
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for lcur in range(1,n-k+1):
            rcur = lcur+k-1
            current_sum = current_sum-nums[lcur-1]+nums[rcur]
            max_sum = max(current_sum,max_sum)
        return max_sum/k

nums = [1,12,-5,-6,50,3]
k=4
print(Solution().findMaxAverage(nums,k))