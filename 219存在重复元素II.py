r'''
给你一个整数数组 nums 和一个整数 k ，
判断数组中是否存在两个 不同的索引 i 和 j ，
满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
如果存在，返回 true ；否则，返回 false 。
'''

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)<=k+1:
            return len(set(nums))<len(nums)
        pool = set(nums[:k+1])
        if len(pool) < k+1:
            return True
        for i in range(k+1,len(nums)):
            pool.remove(nums[i-k-1])
            pool.add(nums[i])
            if len(pool) < k+1:
                return True
        return False
    
s = Solution()
nums = [1]
k=1
print(s.containsNearbyDuplicate(nums,k))